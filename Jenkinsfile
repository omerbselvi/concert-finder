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
            agent {
                docker {
                    image 'selenium/standalone-chrome'
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                    sh 'python find_concert.py -c heavy_metal --city istanbul'
                }
            }
        }
    }
}