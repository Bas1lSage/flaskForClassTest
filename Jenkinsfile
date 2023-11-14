pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'SonarQube'
    }

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
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=ssdQuiz -Dsonar.sources=."
                }
            }
        }
    }
}


