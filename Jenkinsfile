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
                git branch: 'main', url: 'https://github.com/Arya2422/CI-CD-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKERHUB_USER/$IMAGE_NAME:latest ./app'
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --name test_container $DOCKERHUB_USER/$IMAGE_NAME:latest'
                    sh 'sleep 5'
                    sh 'curl http://localhost:5000'
                    sh 'docker stop test_container && docker rm test_container'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                    sh 'docker push $DOCKERHUB_USER/$IMAGE_NAME:latest'
                }
            }
        }
    }

    post {
        success {
            echo "✅ BUILD SUCCESSFUL! 🎉 Docker image pushed to Docker Hub: $DOCKERHUB_USER/$IMAGE_NAME:latest"
        }
        failure {
            echo "❌ BUILD FAILED! Check logs for details."
        }
        always {
            echo "📦 Pipeline completed."
        }
    }
}
