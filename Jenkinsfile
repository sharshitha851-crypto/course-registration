pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t course-registration:v1 .'
            }
        }
    }

    post {
        success {
            echo 'Course Registration v1 pipeline completed successfully!'
        }

        failure {
            echo 'Course Registration v1 pipeline failed.'
        }
    }
}