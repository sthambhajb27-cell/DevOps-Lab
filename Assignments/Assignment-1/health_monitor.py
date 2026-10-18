import docker
import time
import requests

client = docker.from_env()

def check_health_and_restart():
    while True:
        try:
            # Check container status
            container = client.containers.get("flask-app")
            
            # Check application health via HTTP
            response = requests.get("http://localhost:5000/health")
            if response.status_code == 200:
                print("Flask application is healthy.")
            else:
                print("Flask application returned unhealthy status code. Restarting...")
                container.restart()
                
        except requests.exceptions.RequestException:
            print("Failed to connect to Flask application. Restarting container...")
            try:
                container = client.containers.get("flask-app")
                container.restart()
            except docker.errors.NotFound:
                print("Flask container not found! Please run setup script.")
                
        except docker.errors.NotFound:
            print("Flask container not found! Please run setup script.")
            
        time.sleep(10)

if __name__ == "__main__":
    print("Starting container health management...")
    check_health_and_restart()
