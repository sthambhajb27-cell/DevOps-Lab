# Exercise 9: Jenkins Multi-Stage Pipeline

This exercise demonstrates creating a multi-stage CI pipeline in Jenkins.

## Jenkinsfile
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
```

## Steps
1. Create a new Pipeline job in Jenkins.
2. Provide the Jenkinsfile above.
3. Build and view the Stage View to see all three stages execute sequentially.
