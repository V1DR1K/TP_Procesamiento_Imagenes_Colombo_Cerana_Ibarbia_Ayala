# Trabajo práctico 2 - Procesamiento de Imágenes I

**TUIA · UNR · 2026 · Grupo 10**  
Tomas Colombo, Franco Cerana, Juan manuel Ayala y Manuel Ibarbia.

## Estado del trabajo

Está resuelto únicamente el **ejercicio 1.a**: segmentación automática de monedas y dados de `Assets/monedas.jpg`. Los puntos 1.b, 1.c y el problema 2 están pendientes. El informe en Markdown es parcial y deberá ampliarse a medida que se desarrollen los demás puntos; antes de la entrega debe exportarse a PDF.

## Requisitos

- Python 3.12 (probado con 3.12.10).
- NumPy 1.26.4 y OpenCV Python Headless 4.10.0.84 para la segmentación.

En PowerShell, desde la raíz del repositorio, crear el entorno **fuera** de este para mantener la restricción de formatos de la entrega:

```powershell
python -m venv ../entorno_tp2
../entorno_tp2/Scripts/python -m pip install numpy==1.26.4 opencv-python-headless==4.10.0.84
```

En Linux/macOS reemplazar `../entorno_tp2/Scripts/python` por `../entorno_tp2/bin/python`. El programa no requiere interfaz gráfica: guarda todas las etapas como PNG y muestra información de la ejecución en la consola.

## Ejecutar el ejercicio 1.a

```powershell
../entorno_tp2/Scripts/python ejercicio_1/segmentacion_1a.py
```

La entrada predeterminada es `Assets/monedas.jpg`. La salida se guarda en `Assets/resultados/ejercicio_1a/`: original redimensionada, grises suavizada, bordes Canny, cierre morfológico, máscara binaria y regiones numeradas. Para elegir otros archivos:

```powershell
../entorno_tp2/Scripts/python ejercicio_1/segmentacion_1a.py --imagen ruta/imagen.jpg --salida ruta/resultados
```

Los parámetros se ajustaron a la imagen suministrada; otra imagen puede requerir cambios. La máscara usa envolventes convexas aproximadas y no clasifica objetos. Para el archivo provisto se detectan 19 regiones (17 monedas y 2 dados según inspección visual); los números identifican regiones, no valores.

## Informe

El informe parcial se edita en `informe_TP2.md` y utiliza las imágenes de `Assets/resultados/ejercicio_1a/`. Al completar el trabajo, exportarlo a PDF y verificar que las imágenes se visualicen correctamente. El PDF es obligatorio para la entrega.

## Organización y continuidad

- `ejercicio_1/`: script del punto 1.a. La función `segmentar` devuelve imágenes intermedias y contornos en la escala de trabajo; pueden servir de base para el punto 1.b y 1.c.
- `Assets/resultados/ejercicio_1a/`: resultados reproducibles e imágenes incluidas en el informe.
- `Assets/monedas.jpg`, `Assets/img01.png` a `Assets/img12.png`: imágenes provistas para los problemas 1 y 2.
- `material/`: apuntes suministrados, conservados en Markdown para cumplir los formatos de entrega.
- `Assets/TUIA_PDI_TP2_2026_C2 (1).pdf`: enunciado original; `informe_TP2.md`: informe parcial editable.
- `documentacion.md`: decisiones de implementación y continuidad.

La entrega solo admite `.jpg`, `.png`, `.py`, `.pdf` y `.md`. Mantener entornos, cachés y archivos temporales fuera del repositorio; verificar los archivos agregados antes de publicar. No se incluyen notebooks ni archivos de dependencias `.txt`.
