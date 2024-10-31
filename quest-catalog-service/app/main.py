from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.api.v1.endpoints import quest
from app.db import models
from app.db.session import engine
from fastapi.middleware.cors import CORSMiddleware
from app.grpc.quest_server import serve as grpc_serve
import threading
from dotenv import load_dotenv 

# Load environment variables from .env file
load_dotenv()

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Quest Catalog Service",
    description="Service for getting quest information",
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

# Include other routes
app.include_router(quest.router, prefix="/api/v1/quest", tags=["quest"])

app.dependency_overrides[HTTPBearer] = HTTPBearer()

# Start the gRPC server in a separate thread
grpc_thread = threading.Thread(target=grpc_serve, daemon=True)
grpc_thread.start()

# Root route to check if service is running
@app.get("/")
def read_root():
    return {"message": "Quest Catalog Service is running"}