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
                sh 'docker rm -f selenium-hub'
                sh 'docker rm -f selenium-chrome'
                sh 'docker rm -f selenium-edge'
                sh 'docker rm -f selenium-firefox'
                sh 'docker run -d -p 4442-4444:4442-4444 --net jenkins --name selenium-hub selenium/hub:latest'
                sh 'docker run -d --net jenkins --name selenium-chrome -e SE_EVENT_BUS_HOST=selenium-hub \
                    --shm-size="2g" \
                    -e SE_EVENT_BUS_PUBLISH_PORT=4442 \
                    -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 \
                    selenium/node-chrome:latest'
                sh 'docker run -d --net jenkins --name selenium-edge -e SE_EVENT_BUS_HOST=selenium-hub \
                    --shm-size="2g" \
                    -e SE_EVENT_BUS_PUBLISH_PORT=4442 \
                    -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 \
                    selenium/node-edge:latest'
                sh 'docker run -d --net jenkins --name selenium-firefox -e SE_EVENT_BUS_HOST=selenium-hub \
                    --shm-size="2g" \
                    -e SE_EVENT_BUS_PUBLISH_PORT=4442 \
                    -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 \
                    selenium/node-firefox:latest'
                //sh "apt install docker-compose"
                //sh 'docker-compose -f docker-compose-v3-beta-channel.yml up'
                //sh "python selenium_test_script.py"
                //sh 'docker-compose -f docker-compose-v3-beta-channel.yml down'
            }
        }
    }
}


