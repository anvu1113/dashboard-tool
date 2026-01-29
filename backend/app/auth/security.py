from datetime import datetime, timedelta
from typing import Optional, Any, Union
from jose import jwt
from passlib.context import CryptContext
import os

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 1440))
SECRET_KEY = os.environ.get("SECRET_KEY", "secret")
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None, jti: Optional[str] = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    if jti:
        to_encode["jti"] = jti
        
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
