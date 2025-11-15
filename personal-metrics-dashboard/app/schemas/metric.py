#Aqui se define como deben llegar los datos del cliente (lo que recibe el endpoint)
#Define formas de datos, no logica

from pydantic import BaseModel
#Importa date para definir el tipo de dato fecha
from datetime import date

class MetricCreate(BaseModel):
    #Defini datetime como date para que solo acepte fechas
    datetime: date
    category: str
    value: float
    note: str | None = None #opcional