from backend.app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


password = "password123"

hashed = hash_password(password)

print("\nHashed Password:")
print(hashed)


result = verify_password(
    password,
    hashed
)

print("\nPassword Match:")
print(result)


token = create_access_token(
    {
        "sub": "ripta@gmail.com"
    }
)

print("\nJWT Token:")
print(token)