pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                echo 'Code cloned automatically by Jenkins'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
            }
        }
    }
}
