# Exercise 4: Docker Networking

This exercise demonstrates how to create a custom bridge network in Docker and run multiple containers on it so they can communicate using container names.

## Steps

1. Create a bridge network:
   ```bash
   docker network create --driver bridge my-bridge-net
   ```

2. Build the Flask API image:
   ```bash
   docker build -t flask-api .
   ```

3. Run the containers (MySQL, Redis, and our Flask app) on the custom network:
   ```bash
   docker run -d --name mysql --net=my-bridge-net -e MYSQL_ROOT_PASSWORD=root mysql:latest
   docker run -d --name redis --net=my-bridge-net redis:latest
   docker run -d --name flask --net=my-bridge-net -p 5001:5001 flask-api
   ```

4. Test connectivity from the Flask container to others:
   ```bash
   docker exec -it flask bash
   # Inside container:
   ping mysql
   ping redis
   exit
   ```

5. Clean up:
   ```bash
   docker stop mysql redis flask && docker rm mysql redis flask
   docker network rm my-bridge-net
   ```
