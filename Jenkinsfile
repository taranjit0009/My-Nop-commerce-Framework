pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8'
        BROWSER = 'chrome'
        PATH = "${env.PATH};C:\\Python${PYTHON_VERSION.replace('.','')}\\Scripts;C:\\Python${PYTHON_VERSION.replace('.','')}"
        ALLURE_HOME = "C:\\allure" // Make sure Allure is installed here
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Tools') {
            steps {
                script {
                    // Install Allure if not present
                    try {
                        bat 'allure --version'
                    } catch (Exception e) {
                        bat '''
                            echo Installing Allure...
                            curl -o allure.zip https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.zip
                            mkdir "%ALLURE_HOME%"
                            tar -xf allure.zip -C "%ALLURE_HOME%" --strip-components=1
                            del allure.zip
                            setx PATH "%PATH%;%ALLURE_HOME%\\bin"
                        '''
                    }
                }
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
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    python -m pytest -v -s --browser %BROWSER% --alluredir=allure-results testcases/
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '''
                    allure generate allure-results --clean -o allure-report
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
                    // Verify report exists before publishing
                    def reportExists = fileExists 'allure-report/index.html'
                    if (!reportExists) {
                        error "Allure report not found at allure-report/index.html"
                    }
                    publishHTML(
                        target: [
                            allowMissing: false,
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
    }
    post {
        always {
            // Archive test results
            archiveArtifacts artifacts: 'allure-results/**/*'
            // Clean up workspace if needed
            // cleanWs()
        }
    }
}