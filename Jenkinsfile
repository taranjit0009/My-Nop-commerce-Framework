pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8'  // Using stable version
        BROWSER = 'chrome'
        // Add Python to PATH if not already there
        PATH = "${env.PATH};C:\\Python${PYTHON_VERSION.replace('.','')}\\Scripts;C:\\Python${PYTHON_VERSION.replace('.','')}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python') {
            steps {
                bat '''
                    @echo off
                    :: Check if Python is already installed
                    python --version > nul 2>&1
                    if %errorlevel% neq 0 (
                        echo Installing Python...
                        :: Download and install Python silently
                        curl -o python-installer.exe https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
                        start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
                        del python-installer.exe
                    )
                    :: Verify installation
                    python --version
                    pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                    python -m pip install pytest selenium pytest-selenium allure-pytest webdriver-manager
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    python -m pytest -v -s  --browser %BROWSER% --alluredir=allure-results testcases/
                """
            }
            post {
                always {
                    allure report: 'allure-results', results: [[path: 'allure-results']]
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                bat '''
                    allure generate allure-results -o allure-report --clean
                '''
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
                script {
                 // Ensure directory exists
                    bat '''
                         if not exist "allure-report" mkdir allure-report
                    '''
            publishHTML(
                target: [
                    allowMissing: false,  // Changed to false to fail explicitly
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'allure-report',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report'
                ]
            )
        }
    }
}