# Personal Metrics Dashboard

API para rastrear métricas personales.

## Instalación

1. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate 
 # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Documentación

Una vez ejecutando, visita:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Estructura del Proyecto

```
personal-metrics-dashboard/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ core/
│  │  └─ config.py
│  ├─ db/
│  │  ├─ base.py
│  │  └─ session.py
│  ├─ models/
│  │  └─ __init__.py
│  └─ routers/
│     └─ health.py
├─ .gitignore
├─ requirements.txt
└─ README.md
```
