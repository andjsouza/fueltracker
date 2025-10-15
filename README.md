# Fuel Tracker Application

## Overview
The Fuel Tracker application is a web-based tool designed to help drivers record fuel fill-ups and analyze their fuel consumption and costs over time. This application allows users to manage their vehicle data, track fuel expenses, and gain insights into their driving habits.

## Tech Stack
- **Backend**: Python with FastAPI
- **Database**: PostgreSQL
- **Frontend**: Streamlit (for future enhancements)
- **Containerization**: Docker
- **Development Server**: Uvicorn

## Features
- User authentication (sign up, sign in, and profile management)
- Multi-car support for tracking fuel entries
- Detailed fuel entry management (add, edit, delete)
- Statistics and metrics for fuel consumption and costs
- User-friendly dashboards for visualizing data

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Docker and Docker Compose
- PostgreSQL

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd fueltracker
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   Copy the `.env.example` to `.env` and update the values as needed.

4. Run the application using Docker:
   ```
   docker-compose up
   ```

### Usage
- Access the application at `http://localhost:8000`.
- Use the provided endpoints to interact with the API for managing fuel entries, vehicles, and user profiles.

## Directory Structure
- `app/`: Contains the main application code.
- `app/api/`: Contains the API route handlers.
- `app/core/`: Contains core functionalities and configurations.
- `app/db/`: Contains database models and CRUD operations.
- `app/services/`: Contains business logic and calculations.
- `app/tests/`: Contains unit tests for the application.
- `docker-compose.yaml`: Defines the services for Docker.
- `Dockerfile`: Instructions for building the Docker image.
- `requirements.txt`: Lists the project dependencies.
- `.env.example`: Example environment variables.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.