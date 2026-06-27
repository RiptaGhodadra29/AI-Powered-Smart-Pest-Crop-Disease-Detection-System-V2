from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
import hashlib

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# FIX: stable password normalization
# Use raw SHA256 bytes to avoid bcrypt's 72-byte limit
def normalize(password: str) -> bytes:
    return hashlib.sha256(password.encode()).digest()

def hash_password(password: str):
    return pwd_context.hash(normalize(password))

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(normalize(plain_password), hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=60))
    # Use an integer UNIX timestamp for the exp claim so it is JSON-serializable
    to_encode.update({"exp": int(expire.timestamp())})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)