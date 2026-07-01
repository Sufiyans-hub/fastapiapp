from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.users import User
from schemas.users import UserCreate, UserResponse
from database import get_db
from utils.security import hash_password

router = APIRouter (prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register (user: UserCreate, db: Session = Depends(get_db)):
    pass