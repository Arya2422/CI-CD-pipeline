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
            echo '🧩 Starting container test stage...'
            powershell '''
                Write-Host "Testing if Docker image was built successfully..."
                docker images | Select-String "flask-mysql-app"
                
                Write-Host "Checking if port 5000 is available..."
                $portInUse = Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue
                if ($portInUse) {
                    Write-Host "Port 5000 is in use. Please free it before deployment."
                    exit 1
                } else {
                    Write-Host "Port 5000 is available."
                }
            '''
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
