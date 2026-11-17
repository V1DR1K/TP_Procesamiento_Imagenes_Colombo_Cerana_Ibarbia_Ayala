"""Segmentación automática de monedas y dados del TP2, ejercicio 1.a."""
import argparse
from pathlib import Path

import cv2
import numpy as np

RAIZ = Path(__file__).resolve().parents[1]


def guardar(ruta, imagen):
    # imencode permite rutas con caracteres Unicode también en Windows.
    correcto, datos = cv2.imencode('.png', imagen)
    if not correcto:
        raise OSError(f'No se pudo codificar {ruta}')
    datos.tofile(str(ruta))
    print(f'  Imagen guardada: {ruta}')


def segmentar(imagen):
    """Devuelve etapas y contornos en la escala de trabajo de 1200 px."""
    ancho = 1200
    alto = round(imagen.shape[0] * ancho / imagen.shape[1])
    original = cv2.resize(imagen, (ancho, alto), interpolation=cv2.INTER_LINEAR)
    gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    suavizada = cv2.GaussianBlur(gris, (5, 5), 0)
    bordes = cv2.Canny(suavizada, 40, 100)
    elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    cerrados = cv2.morphologyEx(bordes, cv2.MORPH_CLOSE, elemento, iterations=2)
    candidatos, _ = cv2.findContours(cerrados, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos = [cv2.convexHull(c) for c in candidatos if 2000 < cv2.contourArea(c) < 15000]
    contornos.sort(key=lambda c: (cv2.boundingRect(c)[1], cv2.boundingRect(c)[0]))
    mascara = np.zeros(gris.shape, dtype=np.uint8)
    cv2.drawContours(mascara, contornos, -1, 255, cv2.FILLED)
    anotada = original.copy()
    for i, contorno in enumerate(contornos, 1):
        cv2.drawContours(anotada, [contorno], -1, (0, 30, 255), 2)
        x, y, _, _ = cv2.boundingRect(contorno)
        cv2.putText(anotada, str(i), (x, max(18, y - 5)), cv2.FONT_HERSHEY_SIMPLEX, .6, (0, 0, 255), 2, cv2.LINE_AA)
    return {'01_original': original, '02_grises_suavizada': suavizada,
            '03_bordes_canny': bordes, '04_cierre_morfologico': cerrados,
            '05_mascara': mascara, '06_regiones': anotada}, contornos


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--imagen', type=Path, default=RAIZ / 'Assets' / 'monedas.jpg')
    parser.add_argument('--salida', type=Path, default=RAIZ / 'Assets' / 'resultados' / 'ejercicio_1a')
    args = parser.parse_args()
    if not args.imagen.is_file():
        parser.error(f'No existe la imagen: {args.imagen}')
    imagen = cv2.imdecode(np.fromfile(str(args.imagen), dtype=np.uint8), cv2.IMREAD_COLOR)
    if imagen is None:
        parser.error(f'No se pudo leer la imagen: {args.imagen}')
    args.salida.mkdir(parents=True, exist_ok=True)
    etapas, contornos = segmentar(imagen)
    print(f'Entrada: {args.imagen} ({imagen.shape[1]} x {imagen.shape[0]} píxeles)')
    print('Escala de trabajo: 1200 píxeles de ancho; Canny: 40/100; cierre: 7x7, 2 iteraciones.')
    print('Filtro de área de contorno: entre 2000 y 15000 píxeles cuadrados.')
    for nombre, resultado in etapas.items():
        print(f'Etapa: {nombre}')
        guardar(args.salida / f'{nombre}.png', resultado)
    print(f'Regiones segmentadas: {len(contornos)}')
    print('La numeración identifica regiones; no clasifica monedas ni dados.')


if __name__ == '__main__':
    main()

