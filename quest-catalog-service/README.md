# Quest Catalog Service

The Quest Catalog Service is responsible for managing and providing quest information, including details about quest rewards, streak requirements, and duplication limits. This service supports gRPC communication to share quest data with other services, such as the Quest Processing Service.

## Features
- Quest Information Management: Stores and manages details for various quests, including streaks, rewards, and claim limits.
- gRPC Server: Exposes quest data to the Quest Processing Service through gRPC for low-latency, high-performance data retrieval.
- Redis Caching: Caches frequently requested quest data to improve response times and reduce database load.
- Token-Based Authentication: Protects endpoints with JWT authentication, ensuring secure access to quest information.

## Project Structure
```plaintext 
quest-catalog-service/ 
├── app/ 
│ ├── api/ 
│ │ └── v1/ 
│ │   └── endpoints/ 
│ │     └── quest.py             # API routes for managing and retrieving quest information
│ ├── core/ 
│ │ ├── auth.py                  # JWT token validation for authenticated access
│ │ └── config.py                # Configuration settings 
│ ├── db/
│ │ ├── base.py                  # Database base declaration 
│ │ ├── models.py                # Database models for quests, events, and user rewards
│ │ └── session.py               # Database session setup (with pooling) 
│ ├── grpc/
│ │ ├── quest_pb2_grpc.py        # Generated Python Code from the .proto File
│ │ ├── quest_pb2.py             # Generated Python Code from the .proto File
│ │ └── quest_server.py          # gRPC server for quest data retrieval
│ ├── schemas/ 
│ │    ├── quest.py              # Pydantic schemas for request/response validation
│ │    └── reward.py             # Pydantic schemas for request/response validation 
│ ├── services/ 
│ │    └── quest_service.py      # Service layer logic for quest management and retrieval
│ └── main.py                    # Main FastAPI app entry point 
├── kubernetes/ 
│ ├── deployment.yaml            # Kubernetes deployment configuration 
│ └── service.yaml               # Kubernetes service configuration 
├── proto/ 
│ └── quest.proto                # .proto file for gRPC
├── Dockerfile                   # Docker setup for the service 
├── requirements.txt             # Project dependencies 
└── .env                         # Environment variables file 
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/engee-nl/b-code-testing.git
   cd quest-catalog-service
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
    GRPC_SERVER_URL="127.0.0.1:50051"
   ```

## API Endpoints

- **`GET /api/v1/quests/{quest_id}`**
  - **Description**: Retrieve details for a specific quest by id.
  - **Request Body**: `{ "quest_id": "integer" }`
  - **Response**: `{"quest_id": integer, "reward_id": integer, "auto_claim": boolean, "streak": integer, "duplication": integer, "name": string, "description": string, "rewards": object}`

- **`gRPC Endpoint: GetAllQuests`**
  - **Description**: Provides all quest data and rewards to the Quest Processing Service via gRPC.
  - **Request**: `N/A`
  - **Response**: `List of all quests with associated rewards and requirements.`

- **`gRPC Endpoint: GetQuestInfo`**
  - **Description**: Retrieve details for a specific quest by name.
  - **Request**: `{ "quest_name": "string" }`
  - **Response**: `Quest information including name, streak, duplication, auto-claim status, and rewards.`
  
- **`Protected Routes`**:
  - All routes require a Bearer JWT token in the `Authorization` header in the format: `Bearer <token>`.

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8002 --reload --timeout-keep-alive 180
```

## Using Docker

This project can be easily run using Docker. Follow the steps below to get started:

1. **Build the Docker image**:
   Build the Docker image: Navigate to the root of the project directory (where the Dockerfile is located) and run the following command:

   ```
   docker build -t quest-catalog-service-image .
   ```

2. **Run the Docker container**:
   After the image is built, you can run the container using the following command:

   ```
   docker run -d --name quest-catalog-service -p 8002:8002 quest-catalog-service-image
   ```

3. **Access the application**:
   Once the container is running, you can access the application at http://localhost:8002/docs to interact with the API documentation.

4. **Stop the container**:
   To stop the container, use the following command:

   ```
   docker stop quest-catalog-service
   ```

5. **Remove the container (optional)**:
   If you want to remove the container after stopping it, run:

   ```
   docker rm quest-catalog-service
   ```

## Using Kubernetes

Deploying this project with Kubernetes allows you to manage and scale the application efficiently. Follow these steps to get started:

1. **Set up the Kubernetes configuration**:
   Ensure you have the necessary Kubernetes deployment and service configuration files (e.g., deployment.yaml and service.yaml) in the kubernetes/ directory.

2. **Deploy the application**: 
   Apply the configuration files by running the following command in the root directory:

   ```
   kubectl apply -f kubernetes/
   ```

3. **Monitor the deployment**: 
   You can check the status of your pods and services with:

   ```
   kubectl get pods
   kubectl get services
   ```

4. **Access the application**: 
   If using a LoadBalancer service, access the application via the external IP provided by the LoadBalancer. Use the following command to get the external IP:

   ```
   kubectl get services
   ```

5. **Scale the application (optional)**:
   To scale the application, use the following command:

   ```
   kubectl scale deployment <deployment-name> --replicas=<number-of-replicas>
   ```

6. **Delete the deployment (optional)**:
   If you want to remove the deployment, use:

   ```
   kubectl delete -f kubernetes/
   ```

## Using AWS ECR and Deploying with ECS or EKS
AWS ECR allows you to store your Docker images, which can be deployed on ECS or EKS for scalable management. Here is how to deploy:
### **Push the Docker image to ECR**:
   1. **Authenticate** Docker to your ECR registry:
   ```
   aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.<region>.amazonaws.com
   ```
   2. **Tag the Docker image** with your ECR repository URI:
   ```
   docker tag task.io:latest <aws-account-id>.dkr.ecr.<region>.amazonaws.com/task.io:latest
   ```
   3. **Push the image** to your ECR repository:
   ```
   docker push <aws-account-id>.dkr.ecr.<region>.amazonaws.com/task.io:latest
   ```

### **Deploy the image on ECS (Elastic Container Service)**:
   - **Create a new ECS task definition** or update an existing one to use the pushed image from ECR.
   - **Launch the service** in an ECS cluster and configure the desired task scaling.


### **Deploy on EKS (Elastic Kubernetes Service)**:
   - Ensure the EKS cluster is configured to pull from ECR, and update the Kubernetes deployment YAML to point to the ECR image:
   ```
   image: <aws-account-id>.dkr.ecr.<region>.amazonaws.com/task.io:latest
   ```
   - **Apply the updated configuration**:
   ```
   kubectl apply -f kubernetes/deployment.yaml
   ```


## Scaling Recommendations
**Horizontal Scaling**:
   - Use a Load Balancer (e.g., AWS ALB or Nginx) to distribute requests across multiple instances of each service.
   - Use ECS or EKS Fargate to scale automatically (Configure Service Autoscaling in ECS control panel for example).
   
**Caching**:
   - Implement caching (e.g., Redis) in the Quest Catalog Service to store frequently requested quest data.
   
**Database Connection Pooling**:
   - Set up SQLAlchemy connection pooling to manage database connections under high traffic. See **quest-catalog-service/app/db/session.py** file for example.


## Technologies Used
- FastAPI: Web framework for building APIs.
- gRPC: Communication protocol for efficient service-to-service interactions.
- SQLAlchemy: ORM for interacting with the PostgreSQL database.
- PostgreSQL: Database for storing user quest and reward data.
- Redis: Cache for frequently requested quest data.
- JWT: Token-based authentication to secure access.
- Docker: Containerization for consistent deployment.
- Kubernetes: Orchestrates containerized services for scalability.