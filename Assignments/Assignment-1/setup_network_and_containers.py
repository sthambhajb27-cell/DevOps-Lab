import docker
import time

client = docker.from_env()
NETWORK_NAME = "assignment1-network"

def setup_environment():
    # 1. Create a custom bridge network
    try:
        network = client.networks.get(NETWORK_NAME)
        print(f"Network {NETWORK_NAME} already exists.")
    except docker.errors.NotFound:
        network = client.networks.create(NETWORK_NAME, driver="bridge")
        print(f"Created network {NETWORK_NAME}.")

    # 2. Run MongoDB container
    try:
        mongo_container = client.containers.get("mongo")
        print("MongoDB container already running.")
    except docker.errors.NotFound:
        mongo_container = client.containers.run(
            "mongo:latest",
            name="mongo",
            network=NETWORK_NAME,
            detach=True,
            volumes={'mongo_data': {'bind': '/data/db', 'mode': 'rw'}}
        )
        print("Started MongoDB container.")

    # 3. Build and Run Flask container
    print("Building Flask application image...")
    client.images.build(path=".", tag="flask-task-app:latest")
    
    try:
        flask_container = client.containers.get("flask-app")
        print("Flask app container already running.")
    except docker.errors.NotFound:
        flask_container = client.containers.run(
            "flask-task-app:latest",
            name="flask-app",
            network=NETWORK_NAME,
            ports={'5000/tcp': 5000},
            detach=True
        )
        print("Started Flask app container.")

if __name__ == "__main__":
    setup_environment()
