pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_NAME = 'flask-mysql-app'
        DOCKERHUB_USER = 'arya2422'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "📥 Starting to clone repository..."
                git branch: 'main', url: 'https://github.com/Arya2422/CI-CD-pipeline.git'
                echo "✅ Repository cloned successfully from GitHub."
                bat 'dir'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🏗️ Starting Docker image build..."
                script {
                    bat 'docker build -t arya2422/flask-mysql-app:latest ./app'
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    echo "🧩 Starting container test stage..."

                    // Remove existing container if it exists
                    bat 'docker rm -f test_container || exit 0'

                    // Run the new test container
                    bat 'docker run -d -p 5000:5000 --name test_container %DOCKERHUB_USER%/%IMAGE_NAME%:latest'
                    
                    // Wait for the app to start
                    bat 'ping 127.0.0.1 -n 16 > nul'
                    
                    // Check if container is still running
                    bat 'docker ps -f name=test_container'
                    
                    // Check container logs
                    bat 'docker logs test_container'
                    
                    // Test the endpoint
                    bat 'curl -f http://localhost:5000 || (echo ❌ Flask app test failed! && exit 1)'

                    // Stop and remove after test
                    bat 'docker stop test_container && docker rm test_container'
                    echo "✅ Container test completed successfully!"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo "🚀 Logging into Docker Hub..."
                    bat "echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin"
                    echo "📦 Pushing image to Docker Hub..."
                    bat "docker push %DOCKERHUB_USER%/%IMAGE_NAME%:latest"
                    echo "✅ Image pushed successfully to Docker Hub!"
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    echo "🚀 Starting deployment..."
                    
                    // Stop and remove old containers
                    bat 'docker-compose down || exit 0'
                    
                    // Pull the latest image from Docker Hub
                    bat "docker pull %DOCKERHUB_USER%/%IMAGE_NAME%:latest"
                    
                    // Start the application with docker-compose
                    bat 'docker-compose up -d'
                    
                    // Wait for services to start
                    bat 'ping 127.0.0.1 -n 11 > nul'
                    
                    // Verify deployment
                    bat 'docker-compose ps'
                    
                    // Test the deployed application
                    bat 'curl -f http://localhost:5000 || (echo ❌ Deployment verification failed! && exit 1)'
                    
                    echo "✅ Application deployed successfully!"
                }
            }
        }
    }

    post {
        success {
            echo "🎯 BUILD SUCCESSFUL! 🎉"
            echo "🌐 Application is running at http://localhost:5000"
        }
        failure {
            echo "❌ BUILD FAILED! Please check the logs."
            // Cleanup on failure
            bat 'docker-compose down || exit 0'
        }
        always {
            echo "📜 Pipeline completed at ${new Date()}"
        }
    }
}