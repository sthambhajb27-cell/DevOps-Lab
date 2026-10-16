# Exercise 10: Minikube Multi-Node Multi-App Deployment

This exercise demonstrates creating a multi-node cluster in Minikube and deploying multiple applications.

## Steps
1. Start Minikube with 2 nodes:
   ```bash
   minikube start --nodes 2 -p multinode-demo
   ```
2. Verify nodes:
   ```bash
   kubectl get nodes
   ```
3. Deploy an app (e.g., Nginx):
   ```bash
   kubectl create deployment nginx --image=nginx
   kubectl scale deployment nginx --replicas=4
   ```
4. Verify pods are distributed across nodes:
   ```bash
   kubectl get pods -o wide
   ```
