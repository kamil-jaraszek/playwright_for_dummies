pipeline {
  agent {
    docker {
      image 'mcr.microsoft.com/playwright/python:v1.44.0-jammy'
      args '--ipc=host'
    }
  }
  stages {
    stage('Test') {
      steps {
        sh 'pytest -s'
      }
    }
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
