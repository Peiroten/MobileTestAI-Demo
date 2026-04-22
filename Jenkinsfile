pipeline {
    agent any

    environment {
        // Project path on your Jenkins machine (adjust if needed)
        PROJECT_PATH = 'C:\\MobileTestAI-Demo'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Peiroten/MobileTestAI-Demo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
                    cd ${PROJECT_PATH}
                    python -m venv venv
                    call venv\\Scripts\\activate
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    cd ${PROJECT_PATH}
                    call venv\\Scripts\\activate
                    pip install -r requirements.txt
                """
            }
        }

        stage('Start Appium Server') {
            steps {
                bat """
                    start /B appium > appium.log 2>&1
                    timeout /t 10
                """
            }
        }

        stage('Run Mobile Tests') {
            steps {
                bat """
                    cd ${PROJECT_PATH}
                    call venv\\Scripts\\activate
                    python test_scanner_app.py
                """
            }
        }

        stage('Run API Tests') {
            steps {
                bat """
                    cd ${PROJECT_PATH}
                    call venv\\Scripts\\activate
                    python test_api.py
                """
            }
        }
    }

    post {
        always {
            // Stop the Appium server
            bat 'taskkill /F /IM node.exe'

            // Publish test reports (if you have a test framework generating them)
            // junit 'test-results/*.xml'

            // Clean up workspace
            cleanWs()
        }
    }
}