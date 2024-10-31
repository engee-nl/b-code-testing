# User Authentication Service

## Summary
The User Authentication Service is responsible for managing user registration, authentication, and JWT token issuance. 
It is designed to securely handle user credentials and issue tokens for authenticated sessions.

## Features
- User Registration: Allows users to sign up by creating an account with a username and password.
- User Login: Authenticates users and issues JWT tokens for secure session management.
- JWT Token Issuance: Provides a JWT token upon successful login, allowing secure access to other services.
- Token-based Authentication: Protects endpoints and verifies tokens for secure user access.

## Project Structure


## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.

## Environment File
Create a `.env` file in the project root with the following variables:
DATABASE_URL=your-database-url 
SECRET_KEY=your-secret-key 
ACCESS_TOKEN_EXPIRE_MINUTES=30

## Running the Application
- **Locally**: Run `uvicorn app.main:app --reload --port 8001`.
- **Using Docker**:
  - Build: `docker build -t user-auth-service .`
  - Run: `docker run -p 8000:80 user-auth-service`
- **Using Kubernetes**:
  - Deploy: `kubectl apply -f kubernetes/deployment.yaml`

## Technologies Used
- FastAPI
- PostgreSQL (or other SQL database)
- Docker
- Kubernetes
- JWT for token-based authentication
- SQLAlchemy