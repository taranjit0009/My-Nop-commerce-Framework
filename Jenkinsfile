pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.13'  // Updated: Use stable Python version
        BROWSER = 'chrome'      // Default browser
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python${PYTHON_VERSION} -m pip install --upgrade pip
                    python${PYTHON_VERSION} -m pip install -r requirements.txt
                    python${PYTHON_VERSION} -m pip install pytest selenium pytest-selenium allure-pytest webdriver-manager
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    python${PYTHON_VERSION} -m pytest -v -s --browser=${env.BROWSER} --alluredir=allure-results tests/
                """
            }
            post {
                always {
                    allure report: 'allure-results', results: [[path: 'allure-results']]
                }
            }
        }

        stage('Publish HTML Report') {
            when {
                anyOf {
                    equals expected: 'SUCCESS', actual: currentBuild.currentResult
                    equals expected: 'UNSTABLE', actual: currentBuild.currentResult
                }
            }
            steps {
                publishHTML(
                    target: [
                        allowMissing: true,
                        alwaysLinkToLastBuild: false,
                        keepAll: false,
                        reportDir: 'allure-report',
                        reportFiles: 'index.html',
                        reportName: 'Allure Report'
                    ]
                )
            }
        }
    }
}
