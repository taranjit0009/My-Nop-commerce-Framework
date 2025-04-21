pipeline {
    agent any // Run on any available agent

    environment {
        PYTHON_VERSION = '3.x' // Specify your desired Python version
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python') {
            steps {
                script {
                    // Install Python if not already available on the agent
                    if (isUnix()) {
                        sh "sudo apt-get update"
                        sh "sudo apt-get install -y python${PYTHON_VERSION.replace('.x', '')} python${PYTHON_VERSION.replace('.x', '')}-pip"
                    } else {
                        // For Windows, you might need to ensure Python is in the PATH
                        // or use a Jenkins Python Tool configuration
                        echo "Assuming Python is configured in the Windows environment"
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh "python -m pip install --upgrade pip"
                    sh "python -m pip install -r requirements.txt" // Install project dependencies
                    sh "python -m pip install pytest selenium pytest-selenium allure-pytest webdriver-manager" // Install testing dependencies
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Determine the browser to use (can be parameterized)
                    def browser = System.getenv('BROWSER') ?: 'chrome' // Default to chrome if BROWSER env var is not set

                    // Run pytest with specified browser and Allure reporting
                    sh "python -m pytest -v -s --browser=${browser} --alluredir=allure-results tests/"
                }
            }
            post {
                always {
                    allure report: 'allure-results', results: [[path: 'allure-results', keepEmptyDir: false]]
                }
            }
        }

        stage('Publish HTML Report (Optional)') {
            steps {
                // If you generated an HTML report with pytest
                publishHTML([allowMissing: true, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'allure-report', reportFiles: 'index.html', reportName: 'Allure Report'])
            }
            condition: steps.RunTests.result == 'SUCCESS' || steps.RunTests.result == 'UNSTABLE'
        }
    }
}