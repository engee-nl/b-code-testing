# Assignment

This assignment consists of three separate projects: three back-end projects built with Python FastAPI. To simplify sharing, all projects have been combined into a single repository. However, following best practices, each project should ideally be stored in its own separate repository.
A demo section is included at the end of this README.

## Server architecture

If I had access to the necessary servers and time, I would set up the architecture as outlined below. This design is based on the following considerations:
- **Traffic distribution**: Using AWS ECS (or EKS), along with Fargate, helps evenly distribute traffic and optimize resource utilization. 

![Server architecture](server-architecture.drawio.png)

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
