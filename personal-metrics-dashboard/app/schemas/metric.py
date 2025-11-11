#Aqui se define como deben llegar los datos del cliente (lo que recibe el endpoint)
#Define formas de datos, no logica

from pydantic import BaseModel

class MetricCreate(BaseModel):
    datetime: str
    category: str
    value: float
    note: str | None = None #opcional