from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.schemas.user_schema import (
    UserCreate,
    UserLogin
)
from backend.app.schemas.token_schema import Token

from backend.app.services.auth_service import (
    create_user,
    authenticate_user
)

from backend.app.core.auth import create_access_token
from backend.app.database.session import get_db

router = APIRouter()


# -------------------------
# REGISTER API
# -------------------------
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    db_user = create_user(
        db=db,
        username=user.username,
        email=user.email,
        password=user.password
    )

    return {
        "message": "User created successfully",
        "user_id": db_user.id
    }


# -------------------------
# LOGIN API
# -------------------------
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = authenticate_user(db, user.email, user.password)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }