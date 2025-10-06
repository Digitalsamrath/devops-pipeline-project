pipeline {
    agent any

    environment {
        // Defines the name for our custom Docker image
        DOCKER_IMAGE_NAME = "devops-demo-ai-app"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub...'
                // This command pulls the latest code from your repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker image for the AI app...'
                // This command builds the Docker image using the Dockerfile in the 'app' directory
                sh "docker build -t ${DOCKER_IMAGE_NAME} ./app"
            }
        }

        stage('Deploy Services') {
            steps {
                echo 'Deploying AI app using Docker Compose...'
                // This command stops any old containers and starts new ones with the latest code
                sh "docker-compose down && docker-compose up -d"
            }
        }

        stage('Cleanup Old Images') {
            steps {
                echo 'Cleaning up old, unused Docker images...'
                // This is a good practice to save disk space on the server
                sh 'docker image prune -af'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}