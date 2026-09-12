# Exercise 1: Hello Pod

This exercise demonstrates how to run a simple Nginx pod in Kubernetes and expose it as a service.

## Prerequisites
- Minikube running (`minikube start`)
- kubectl installed

## Declarative Approach (Recommended)

1. Apply the Pod manifest:
   ```bash
   kubectl apply -f pod.yaml
   ```

2. Apply the Service manifest:
   ```bash
   kubectl apply -f service.yaml
   ```

3. Access the service:
   ```bash
   minikube service hello-k8s
   ```

## Imperative Approach (Quick)

1. Create Pod:
   ```bash
   kubectl run hello-k8s --image=nginx --port=80
   ```

2. Expose Service:
   ```bash
   kubectl expose pod hello-k8s --type=NodePort --port=80
   ```

3. Access the service:
   ```bash
   minikube service hello-k8s
   ```
