# Exercise 7: Jenkins CI Automation

This exercise introduces Continuous Integration (CI) and walks you through installing Jenkins via Docker.

## Steps to install Jenkins

1. Run the Jenkins Docker container:
   ```bash
   docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
   ```

2. Retrieve the initial admin password:
   ```bash
   docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
   ```

3. Access Jenkins:
   Open your browser and navigate to `http://localhost:8080/`. Paste the initial admin password to unlock Jenkins and complete the setup wizard.
