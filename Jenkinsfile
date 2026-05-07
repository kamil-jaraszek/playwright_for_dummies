pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    playwright install
                '''
            }
        }

        stage('Run Playwright test') {
            steps {
                sh '''
                    python3 -m pytest test/test_jarasznikos.py \
                        --slowmo 1500 \
                        -s

                '''
            }
        }
    }
}
