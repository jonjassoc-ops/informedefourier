# Simulación y análisis de señales con Fourier

Este proyecto analiza un pulso rectangular, un escalón unitario y un seno de 5 Hz en los dominios del tiempo y la frecuencia. Grafica magnitud y fase, y verifica la linealidad, el desplazamiento temporal y el escalamiento temporal del pulso.

## Requisitos
Python 3.10 o posterior, NumPy y Matplotlib. Instala con `python -m pip install -r requirements.txt`.

## Ejecución
Desde esta carpeta, ejecuta `python simulacion_fourier.py`. El programa imprime resolución y errores de las propiedades, y guarda PNG en `figuras/`.

## Método y alcance
La frecuencia de muestreo es 1 kHz y la observación dura 1 s. `dt * FFT` aproxima la transformada continua. El escalón está limitado a una ventana finita y su espectro muestra truncamiento y fuga espectral. El corrimiento circular corresponde a la DFT. La propiedad de escala temporal se interpreta con `x(a t) ↔ (1/|a|) X(f/a)`: comprimir en tiempo extiende el espectro y reduce su amplitud por el factor correspondiente.

## Publicación en GitHub
Crea un repositorio vacío y ejecuta desde esta carpeta, reemplazando la URL:

```bash
git init
git add .
git commit -m "Agregar simulación de transformada de Fourier"
git branch -M main
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```

Reemplaza `[Nombre del estudiante]` en el informe y la presentación antes de entregar.


