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
        stage('OWASP Dependency Check') {
            steps {
                dependencyCheck additionalArguments: ''' 
                            --enableExperimental
                            -o './'
                            -s './webApp'
                            -f 'XML' 
                            ''', odcInstallation: 'default'

                // Write report to specified file
                dependencyCheckPublisher pattern: 'dependency-check-report.xml'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=ssdQuiz -Dsonar.sources=."
                }
            }
        }
        stage('Selenium') {
            steps {
                sh 'docker-compose -f docker-compose-v3-beta-channel.yml up'
                //sh "python selenium_test_script.py"
                sh 'docker-compose -f docker-compose-v3-beta-channel.yml down'
            }
        }
    }
}


