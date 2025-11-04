pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-login')
        IMAGE_NAME = "yourdockerhubusername/flask-mysql-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME:latest ./app'
                }
            }
        }

        stage('Run Container for Testing') {
            steps {
                script {
                    sh 'docker run -d --name test_app -p 5000:5000 $IMAGE_NAME:latest'
                    sh 'sleep 10'
                    sh 'curl -f http://localhost:5000 || exit 1'
                    sh 'docker stop test_app && docker rm test_app'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }

        stage('Deploy (Optional)') {
            steps {
                echo 'Deployment stage — can be extended for servers, EC2, or Kubernetes.'
            }
        }
    }
}
