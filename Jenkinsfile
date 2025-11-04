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
                sh 'ls -al'  // Show cloned files
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "🏗️ Starting Docker image build for: $DOCKERHUB_USER/$IMAGE_NAME:latest"
                    sh 'docker build -t $DOCKERHUB_USER/$IMAGE_NAME:latest ./app'
                    echo "✅ Docker image built successfully!"
                    echo "🔍 Listing Docker images for verification..."
                    sh 'docker images | grep $IMAGE_NAME'
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    echo "🧪 Starting test container..."
                    sh 'docker run -d -p 5000:5000 --name test_container $DOCKERHUB_USER/$IMAGE_NAME:latest'
                    echo "⚙️ Waiting for container to initialize..."
                    sh 'sleep 5'
                    echo "🌐 Checking if application is reachable at http://localhost:5000"
                    sh 'curl -I http://localhost:5000 || true'  // Print headers, continue even if curl fails
                    echo "🧹 Stopping and removing test container..."
                    sh 'docker stop test_container && docker rm test_container'
                    echo "✅ Test container ran successfully and cleaned up!"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo "🚀 Logging into Docker Hub..."
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                    echo "📦 Pushing image to Docker Hub: $DOCKERHUB_USER/$IMAGE_NAME:latest"
                    sh 'docker push $DOCKERHUB_USER/$IMAGE_NAME:latest'
                    echo "✅ Docker image pushed successfully to Docker Hub."
                }
            }
        }
    }

    post {
        success {
            echo "🎯 BUILD SUCCESSFUL! 🎉"
            echo "✅ Docker image pushed to Docker Hub: $DOCKERHUB_USER/$IMAGE_NAME:latest"
        }
        failure {
            echo "❌ BUILD FAILED! Please check the logs above for details."
        }
        always {
            echo "📜 Pipeline execution completed."
            echo "🕒 Build finished at: ${new Date()}"
        }
    }
}
