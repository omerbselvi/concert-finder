pipeline {
    agent none
    stages {
        stage('checkout') {
            agent {
                node {
                    label 'master'
                }
            }
            steps {
                checkout scm
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
                    sh 'dpkg -i google-chrome-stable_current_amd64.deb'
                    sh 'pip install --user -r requirements.txt'
                    sh 'python find_concert.py -c heavy_metal --city istanbul'
                }
            }
        }
    }
}