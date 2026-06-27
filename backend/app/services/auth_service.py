from sqlalchemy.orm import Session
from backend.app.models.user import User
from backend.app.core.security import hash_password, verify_password


def create_user(db: Session, username: str, email: str, password: str):

    hashed_pw = hash_password(password)

    new_user = User(
        username=username,
        email=email,
        password_hash=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user