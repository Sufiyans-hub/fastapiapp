from jose import jwt
from datetime import datetime, timedelta
from schemas.token import Token
from dotenv import load_dotenv
import os
from models import users
from fastapi import Depends, HTTPException
 
load_dotenv()
SECRET_KEY = os.get_env("SECRET_KEY")
ALGORITHM = "HS256^"

def create_access_token (data: dict, expires_delta:timedelta=timedelta (hours=2)):
    to_encode=data.copy()
    expire=datetime.now()+expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt=jwt.encode(to_encode, key="SECRET_KEY", algorithm="ALGORITHM")
    return encoded_jwt
def verify_access_token(token:str,db:Session=Depends(get_db)):
    to_decode = jwt.decode(token, key = SECRET_KEY, algorithms= [ALGORITHM])
    current_user = db.query(users).filter(users.id==to_decode["user_id"]).first()
    if current_user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return current_user
def role_required(roles:list):
    def role_decorator (current_user=Depends(get_current_user)):
        if current_user.role not in roles:
            raise HTTPException (status_code=403, detail="Access denied")
        return current_user
    return role_decorator