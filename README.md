# Assignment

This assignment consists of three separate projects: three back-end projects built with Python FastAPI. To simplify sharing, all projects have been combined into a single repository. However, following best practices, each project should ideally be stored in its own separate repository.
A demo section is included at the end of this README.

# Task
- **<API Request and DB Query>**
Given the DB schema (see below) create an endpoint for the signup request to handle a ‘sign-in three-times’ quest. 
You should keep track of the middle actions that happen before completing a quest. 

In particular, suppose there is a 'sign-in-three-times' quest. 
This quest gives as reward 10 diamonds if the user logs in 3 times, and you can only receive a reward manually (claiming rewards is out of the scope), and you can get this reward up to 2 times. In this case, it has false auto-claim and 3 streaks and 2 duplication.

## Server architecture

If I had access to the necessary servers and time, I would set up the architecture as outlined below. This design is based on the following considerations:
- **Traffic distribution**: Using AWS ECS (or EKS), along with Fargate, helps evenly distribute traffic and optimize resource utilization. 
- **gRPC Communication**: Implement gRPC for efficient, low-latency communication between the Quest Catalog Service and Quest Processing Service. This makes it quick to retrieve quest details and supports real-time data sharing.
- **Redis Caching for Quest Catalog Service**: Use Redis to cache frequently requested quest data, minimizing database queries and reducing latency for high-traffic requests. This improves the performance and scalability of the Quest Catalog Service by serving cached responses when possible. 
- **JWT Token for Authentication Across Services**: Use JWT (JSON Web Tokens) to authenticate requests across all services, ensuring secure, token-based access. Each service validates JWT tokens on incoming requests to enforce security and user authentication consistently.

![Server architecture](server-architecture.drawio.png)


## Updated Database Schema


## Back-end : User Authentication Service

Service for user registration and login

## Back-end : Quest Catalog Service

Service for getting quest information

## Back-end : Quest Processing Service

Service for tracking user quests and managing rewards

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.
