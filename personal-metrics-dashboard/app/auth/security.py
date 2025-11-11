#Aqui se encarga de cifrar y verificar contraseñas
#Usa bcrypt.hashpw y bcrypt.checkpw 

import bcrypt

def hash_password(plain_password: str) -> str:
    """Cifra una contraseña en texto plano usando bcrypt."""
    # Generar un salt
    salt = bcrypt.gensalt()
    # Cifrar la contraseña
    hashed = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica una contraseña en texto plano contra una contraseña cifrada."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))