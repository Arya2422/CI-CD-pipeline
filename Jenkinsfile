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
                bat 'dir'  // Windows equivalent of 'ls -al'
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
                    echo "🧪 Starting test container..."
                    bat "docker run -d -p 5000:5000 --name test_container %DOCKERHUB_USER%/%IMAGE_NAME%:latest"
                    echo "⚙️ Waiting for container to initialize..."
                    bat 'timeout /t 10'
                    echo "🌐 Checking if application is reachable..."
                    bat 'curl http://localhost:5000'
                    echo "🧹 Cleaning up test container..."
                    bat 'docker stop test_container && docker rm test_container'
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
                }
            }
        }
    }

    post {
        success {
            echo "🎯 BUILD SUCCESSFUL! 🎉"
        }
        failure {
            echo "❌ BUILD FAILED! Please check the logs."
        }
        always {
            echo "📜 Pipeline completed at ${new Date()}"
        }
    }
}
