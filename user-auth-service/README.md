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

1. Clone the repository:
   ```bash
   git clone https://github.com/engee-nl/b-code-testing.git
   cd user-auth-service
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r app/requirements.txt
   ```

4. Create a `.env` file with your environment variables:
   ```plaintext
    DATABASE_ONE_URL="REDACTED"
    QUEST_PROC_SERVICE_URL="http://127.0.0.1:8003/api/v1/track"
    QUEST_CATA_SERVICE_URL="http://127.0.0.1:8002/api/v1/quest"
    USER_AUTH_SERVICE_URL="http://127.0.0.1:8001/api/v1/auth"
   ```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload --timeout-keep-alive 180
```

## Using Docker

This project can be easily run using Docker. Follow the steps below to get started:

1. **Build the Docker image**:
   Build the Docker image: Navigate to the root of the project directory (where the Dockerfile is located) and run the following command:

   ```
   docker build -t user-auth-service-image .
   ```

2. **Run the Docker container**:
   After the image is built, you can run the container using the following command:

   ```
   docker run -d --name user-auth-service -p 8001:8001 user-auth-service-image
   ```

3. **Access the application**:
   Once the container is running, you can access the application at http://localhost:8001/docs to interact with the API documentation.

4. **Stop the container**:
   To stop the container, use the following command:

   ```
   docker stop user-auth-service
   ```

5. **Remove the container (optional)**:
   If you want to remove the container after stopping it, run:

   ```
   docker rm user-auth-service
   ```
## Using Kubernetes
  - Deploy: `kubectl apply -f kubernetes/deployment.yaml`

## Technologies Used
- FastAPI
- PostgreSQL (or other SQL database)
- Docker
- Kubernetes
- JWT for token-based authentication
- SQLAlchemy