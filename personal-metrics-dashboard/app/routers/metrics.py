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
def list_metrics():
    pass

@router.delete("/{id}")
def delete_metric():
    pass
