# Exercise 3: Scaling Flask App with ReplicaSets

This exercise demonstrates how to deploy an application (Flash Sale app) using a ReplicaSet and scale it dynamically.

## Steps

1. Point your Docker daemon to Minikube:
   ```bash
   eval $(minikube docker-env)
   ```

2. Build the Docker image locally within Minikube:
   ```bash
   docker build -t flashsale:1.0 .
   ```

3. Apply the ReplicaSet and Service:
   ```bash
   kubectl apply -f flashsale-replicaset.yaml
   ```

4. Verify the ReplicaSet and Pods:
   ```bash
   kubectl get rs
   kubectl get pods
   ```

5. Scale the ReplicaSet to 5 replicas:
   ```bash
   kubectl scale rs flashsale-rs --replicas=5
   ```

6. Verify the new Pods are created:
   ```bash
   kubectl get pods
   ```

7. Simulate a Pod failure by deleting one Pod, and observe Kubernetes automatically recreating it:
   ```bash
   kubectl delete pod <pod-name>
   kubectl get pods
   ```

8. Access the service using port-forwarding (since it's a ClusterIP):
   ```bash
   kubectl port-forward svc/flashsale-svc 8080:80
   ```
   Then open `http://localhost:8080/buy` in your browser to see different pods serving the requests.
