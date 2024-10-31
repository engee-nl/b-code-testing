from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.core.config import settings

# Define the JWT security scheme
security = HTTPBearer()

def verify_token(token: str):
    try:
        # Decode the JWT token
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload  # Return the token's payload if verification succeeds
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

'''
async def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")
    if auth_header is None or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Authorization header missing or incorrect format")

    token = auth_header.split(" ")[1]  # Extract the token from "Bearer <token>"
    return verify_token(token)
'''

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    return verify_token(token)