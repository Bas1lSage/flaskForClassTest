pipeline {
    agent any

    stages {
        stage('Build') { 
            steps {
                sh 'docker build -t webapp:latest webApp/'
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


