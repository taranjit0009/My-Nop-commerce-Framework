pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8'
        BROWSER = 'chrome'
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
                    python --version > nul 2>&1
                    if %errorlevel% neq 0 (
                        echo Installing Python...
                        curl -o python-installer.exe https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
                        start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
                        del python-installer.exe
                    )
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
                    python -m pip install allure-python-commons
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    python -m pytest -v -s --browser %BROWSER% --alluredir=allure-results testcases/
                """
            }
            post {
                always {
                    // Clean existing results to prevent conflicts
                    cleanWs()
                    // Generate and publish Allure report
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }
}