# Assignment 1: Dockerized Multi-Container Web Application

This assignment implements a Python Flask CRUD web application with a MongoDB backend, managed via the Docker Python SDK.

## Prerequisites
- Docker installed and running
- Python 3 with `docker` and `requests` packages installed (`pip install docker requests`)

## How to run

1. Run the setup script to create the custom Docker network, start the MongoDB database with persistent volumes, and build/run the Flask application:
   ```bash
   python setup_network_and_containers.py
   ```

2. Once the containers are running, you can interact with the CRUD API:
   - Create a task: `curl -X POST -H "Content-Type: application/json" -d '{"id":"1","title":"Complete DevOps Assignment"}' http://localhost:5000/tasks`
   - Read tasks: `curl http://localhost:5000/tasks`

3. In a separate terminal, run the health monitor script to ensure the Flask container is healthy:
   ```bash
   python health_monitor.py
   ```
   If the container stops or the `/health` endpoint fails, the script will automatically restart it.
