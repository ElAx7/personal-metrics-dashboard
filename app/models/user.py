#Aqui se define como se guarda un usuario en la base de datos
#ORM = Object Relational Mapping

from app.db.base import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    #hashed_password no deber ser la contraseña real. En la autenticacion se
    #compara la version "hasheada"
    hashed_password = Column(String, nullable=False)
    created_at = Column(String, nullable=False)


