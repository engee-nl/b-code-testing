from fastapi import FastAPI
from app.api.v1.endpoints import auth
from app.db import models
from app.db.session import engine
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv 

# Load environment variables from .env file
load_dotenv()

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="User Authentication Service",
    description="Service for user registration and login",
    version="1.0.0"
)

# Allow CORS for specific origins
origins = ["http://localhost:3000", "http://127.0.0.1:8001", "http://127.0.0.1:8002", "http://127.0.0.1:8003"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include authentication routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

# Root route to check if service is running
@app.get("/")
def read_root():
    return {"message": "User Authentication Service is running"}