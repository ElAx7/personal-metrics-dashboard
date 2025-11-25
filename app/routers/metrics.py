from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models_base import Metric
from app.schemas.metric import MetricCreate, MetricUpdate

router = APIRouter(prefix="/metrics", tags=["metrics"])


# -------- CREATE --------
@router.post("/")
def create_metric(metric: MetricCreate, db: Session = Depends(get_db)):
    new_metric = Metric(**metric.model_dump())
    db.add(new_metric)
    db.commit()
    db.refresh(new_metric)
    return new_metric


# -------- LIST --------
@router.get("/")
def list_metrics(db: Session = Depends(get_db)):
    return db.query(Metric).all()


# -------- FILTER --------
@router.get("/filter")
def filter_metrics(
    category: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Metric)

    if category:
        query = query.filter(Metric.category == category)

    if start_date:
        query = query.filter(Metric.datetime >= start_date)

    if end_date:
        query = query.filter(Metric.datetime <= end_date)

    return query.all()


# -------- GET ONE --------
@router.get("/{id}")
def get_metric(id: int, db: Session = Depends(get_db)):
    metric = db.query(Metric).filter(Metric.id == id).first()
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")
    return metric


# -------- UPDATE --------
@router.put("/{id}")
def update_metric(id: int, data: MetricUpdate, db: Session = Depends(get_db)):
    metric = db.query(Metric).filter(Metric.id == id).first()

    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(metric, key, value)

    db.commit()
    db.refresh(metric)
    return metric


# -------- DELETE --------
@router.delete("/{id}")
def delete_metric(id: int, db: Session = Depends(get_db)):
    metric = db.query(Metric).filter(Metric.id == id).first()

    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")

    db.delete(metric)
    db.commit()
    
    return {"detail": "Metric deleted"}
