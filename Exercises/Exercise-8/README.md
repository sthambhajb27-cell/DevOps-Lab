# Exercise 8: Jenkins Hello World Job

This exercise demonstrates creating a basic Jenkins freestyle project or pipeline to print "Hello World".

## Steps
1. Log in to Jenkins.
2. Click "New Item" -> enter name "Hello-World" -> select "Pipeline".
3. In the Pipeline section, add:
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Hello') {
               steps {
                   echo 'Hello World'
               }
           }
       }
   }
   ```
4. Click "Save" and "Build Now".
5. Check the Console Output to see "Hello World".
