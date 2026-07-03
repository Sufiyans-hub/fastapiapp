#schemas/token.py

from pydantic import BaseModel

class Token(BaseModel):
    token: str
    token_type: str

#utils/tokens.py

from jose import jwt
from datetime import datetime, timedelta
from schemas.token import Token

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, key="your_secret_key", algorithm="HS256")
    return encoded_jwt