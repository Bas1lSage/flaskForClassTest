pipeline {
    agent any

    stages {
        stage('Build') { 
            steps {
                sh 'docker build -f webApp/Dockerfile -t webapp:latest .' 
            }
        }
        stage('Deploy') { 
            steps { 
                sh 'docker rm -f webapp'
                sh 'docker run -d -p 3000:3000 --name webapp webapp'
            }
        }
    }
}


