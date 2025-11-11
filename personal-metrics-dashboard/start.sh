#!/bin/bash

# Activar entorno virtual
source venv/bin/activate

# Arrancar servidor
uvicorn app.main:app --reload --port 8000

# Comando alternativo si el archivo main.py está en el directorio raíz
uvicorn main:app --reload
# Explicación:
# uvicorn es el servidor ASGI.
# main es el nombre del archivo (sin .py).
# app es el objeto FastAPI que definiste en ese archivo.
# --reload hace que el servidor se reinicie automáticamente 
# cuando cambies el código.