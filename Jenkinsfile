pipeline {
    agent any



    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python venv') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    playwright install
                '''
            }
        }

        stage('Run Playwright test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 -m pytest test/test_flightrising.py \
                        --headed \
                        --slowmo 1500 \
                        -m klikacz_general \
                        --username=Jarasznikos \
                        --password=toechodioler
                '''
            }
        }
    }
}
