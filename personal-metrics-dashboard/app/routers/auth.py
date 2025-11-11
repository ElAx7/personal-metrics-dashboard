#Aqui expone los endpoints que usan lo anterior.
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

#Endpoints
@router.post("/register")
@router.post("/login")

#Para /me, se necesita una dependecia de autenticacion
@router.get("/me")
def read_current_user():
    pass

