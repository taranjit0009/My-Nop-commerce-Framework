pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8'
        BROWSER = 'chrome'
        // Add Python to PATH if not already there
        PATH = "${env.PATH};C:\\Python${PYTHON_VERSION.replace('.','')}\\Scripts;C:\\Python${PYTHON_VERSION.replace('.','')}"
        ALLURE_RESULTS = 'allure-results'
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
                    python -m pip install pytest selenium pytest-selenium allure-pytest webdriver-manager allure-python-commons
                '''
            }
        }

        stage('Clean Workspace') {
            steps {
                // Clean previous Allure results
                bat "if exist ${ALLURE_RESULTS} rmdir /s /q ${ALLURE_RESULTS}"
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    python -m pytest -v -s testcases --browser %BROWSER% --alluredir=${ALLURE_RESULTS} --clean-alluredir
                """
            }
        }

        stage('Verify Allure Results') {
            steps {
                // Debugging step to verify JSON files were generated
                bat "dir /s /b ${ALLURE_RESULTS}\\*.*"
            }
        }

        stage('Publish Allure Report') {
            steps {
                script {
                    // Generate and publish Allure report
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: "${ALLURE_RESULTS}"]]
                    ])
                }
            }
        }
    }

    post {
        always {
            // Archive test results for debugging
            archiveArtifacts artifacts: "${ALLURE_RESULTS}/**/*.*", allowEmptyArchive: true
        }
    }
}