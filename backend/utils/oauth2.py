from fastapi import OAuth2PasswordBearer, Depends, HTTPException
from database import get_db
from sqlalchemy import text
from sqlalchemy.orm import Session
from utils.token import verify_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str=Depends(oauth2_scheme), db:Session=Depends(get_db)):
    current_user = verify_token(token)
    if current_user is None:
        raise HTTPException(status_code = 401, detail = "Invalid Credentials")
    return current_user