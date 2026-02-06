# recorta-videos-
en si lo cree para recortar videos con decimales por aburrimiento ( funciona solo en linux) bueno mi recomedacion para videos de tiktok son 2.25 segundos

---

# Recorte automático de últimos segundos de vídeos (Python + ffmpeg)

Script en Python para procesar vídeos en lote: recorta los últimos N segundos de cada archivo de una carpeta y guarda el resultado en otra carpeta, manteniendo los originales intactos.

## Estructura esperada

```
automatizaciones/
├── venv/
├── trim_lote.py
├── videoscompletos/      # vídeos originales
└── videosincompletos/    # vídeos recortados (salida)
```

## Requisitos

* Python 3.10+
* ffmpeg y ffprobe instalados en el sistema
* Entorno virtual Python
* Librería tqdm
* Linux debian ( no lo he probado en otras licencias) 

Instalación típica:

```bash
sudo apt install ffmpeg python3-venv
python3 -m venv venv
source venv/bin/activate
pip install tqdm
```

## Funcionamiento

* Lee todos los vídeos de `videoscompletos/`
* Calcula la duración con ffprobe
* Resta los segundos indicados (admite decimales)
* Recorta con ffmpeg
* Guarda el vídeo recortado en `videosincompletos/`
* No modifica los originales
* Muestra barra de progreso

## Uso

Activar entorno:

```bash
source venv/bin/activate
```

Ejecutar:

```bash
python trim_lote.py
```

Introducir segundos a recortar, por ejemplo:

```
2.5
```

## Formatos soportados

```
mp4, mkv, avi, mov, webm, flv
```

Ventajas:

* Muy rápido
* Sin recodificación

Limitación:

* El corte puede ajustarse al keyframe más cercano (no siempre milisegundo exacto).

Si se requiere corte exacto, modificar el script para recodificar vídeo y audio.

## Seguridad

* El archivo de salida se escribe primero como temporal
* Luego se renombra de forma atómica
* Si ffmpeg falla, no se genera archivo final
