# Exercise 2: Minikube Kubectl Flask

This exercise demonstrates deploying a simple Python Flask application to Minikube.

## Steps

1. Start Minikube:
   ```bash
   minikube start
   ```

2. Point your Docker daemon to Minikube:
   ```bash
   eval $(minikube docker-env)
   ```

3. Build the Docker image locally within Minikube:
   ```bash
   docker build -t flask-app:latest .
   ```

4. Apply the Kubernetes Deployment and Service:
   ```bash
   kubectl apply -f flask-deployment.yaml
   ```

5. Access the application:
   ```bash
   minikube service flask-app-service
   ```
