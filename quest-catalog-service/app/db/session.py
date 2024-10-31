from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Configure the database engine with connection pooling parameters
engine = create_engine(
    settings.DATABASE_TWO_URL,
    pool_size=10,                  # Maximum number of connections in the pool
    max_overflow=20,               # Additional connections that can be opened beyond pool_size
    pool_timeout=30,               # Timeout for getting a connection from the pool
    pool_recycle=1800              # Recycle connections after 30 minutes to avoid stale connections
)

# Set up the sessionmaker using the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
