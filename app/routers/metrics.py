from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models_base import Metric
from app.schemas.metric import MetricCreate


router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.post("/")
def create_metric(metric: MetricCreate, db: Session = Depends(get_db)):
    # Create a new metric in the database
    new_metric = Metric(**metric.dict())
    # Add the new metric to the database session
    db.add(new_metric)
    # Commit the session to save the metric
    db.commit()
    # Refresh the instance to get the updated data
    db.refresh(new_metric)
    # Return the newly created metric
    return new_metric
    
    
@router.get("/")
def list_metrics(metric = Depends(MetricCreate), db: Session = Depends(get_db)):
    return db.query(Metric).all()

@router.get("/filter")
def filter_metrics(
    category: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Metric)

    # Filtrar por categoría
    if category:
        query = query.filter(Metric.category == category)

    # Filtrar por rangos
    if start_date:
        query = query.filter(Metric.datetime >= start_date)

    if end_date:
        query = query.filter(Metric.datetime <= end_date)

    return query.all()

@router.put("/metrics/{id}")
def metricUpdate(id: int, db: Session = Depends(get_db)):
    #Busca la metrica en la base de datos
    find_metric = db.query(Metric)
    #Recibe datos opcionales por body
    
    #Actualiza solo los campos enviados

    #Guarda solo los campos enviados

    #Guarda los cambios
    db.commit()
    #Devuelva la metrica actualizada

@router.delete("/{id}")
def delete_metric(id: int, db: Session = Depends(get_db)):
    metric = db.query(Metric).filter(Metric.id == id).first()
    if metric is None:
        return {"HTTP 404 Not Found"}
    else:
        db.delete(metric)
        db.commit()
        return {"Success: Metric deleted"}
