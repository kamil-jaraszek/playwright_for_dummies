pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }


        stage('Run Playwright test') {
            steps {
                sh '''
                    python3 -m pytest test/test_flightrising.py \
                        --headed \
                        --slowmo 1500 \
                        -m klikacz_general \
                        --username=Jarasznikos \
                        --password=$toechodioler
                '''
            }
        }
    }
}
