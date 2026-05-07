pipeline {
  agent {
    docker {
      image 'mcr.microsoft.com/playwright/python:v1.44.0-jammy'
      args '--ipc=host --shm-size=1g'
    }
  }

  environment {
    # Wymuś headless na CI (opcjonalne)
    HEADLESS = 'true'
    # Przydatne, jeśli chcesz debugować (ustaw na 'false' lokalnie)
    SLOWMO = '1500'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install dependencies') {
      steps {
        sh '''
          python -m pip install --upgrade pip
          pip install -r requirements.txt || true
          # Playwright browsers są już zainstalowane w obrazie, ale jeśli chcesz:
          # playwright install --with-deps
        '''
      }
    }

    stage('Run Playwright test') {
      steps {
        sh '''
          export HEADLESS=${HEADLESS}
          python3 -m pytest test/test_jarasznikos.py \
            --slowmo ${SLOWMO} \
            -s
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'jarasznikos_storage.json', allowEmptyArchive: true
    }
  }
}
