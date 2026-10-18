# Assignment 2: TreasureBook Deployment

This assignment implements the TreasureBook graph API, deployed to Kubernetes with autoscaling (HPA).

## Steps to Deploy

1. Enable the metrics server in Minikube (required for HPA):
   ```bash
   minikube addons enable metrics-server
   ```

2. Point Docker to Minikube and build the API image:
   ```bash
   eval $(minikube docker-env)
   docker build -t treasurebook-api:latest .
   ```

3. Apply the MongoDB deployment and service:
   ```bash
   kubectl apply -f mongo-deployment.yaml
   ```

4. Apply the TreasureBook API deployment, service, and HPA:
   ```bash
   kubectl apply -f api-deployment.yaml
   kubectl apply -f hpa.yaml
   ```

5. Access the application:
   ```bash
   minikube service treasurebook-service
   ```

## Simulating Traffic (Autoscaling)
To test the HPA, you can run a temporary busybox pod to generate traffic and observe the pod scaling up to 10 replicas:
```bash
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://treasurebook-service; done"
```
Check HPA status:
```bash
kubectl get hpa
kubectl get pods
```
