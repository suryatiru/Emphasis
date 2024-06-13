pipeline {
    agent any

    stages {
        stage('Step 1') {
            steps {
                echo 'Step 1'
                bat 'java -version'
            }
        }
        stage('Step 2') {
            steps {
                echo 'Step 2'
                bat 'git --version'
            }
        }
        stage('Cloning Repo') {
            steps {
                echo 'Step 3'
                git branch: 'graph_feature', url: 'https://github.com/suryatiru/Emphasis.git'
            }
        }
        // stage('Install Dependencies') {
        //     steps {
        //         bat 'pip install -r yfinance'
        //     }
        // }
        stage('Build') {
            steps {
                echo 'Step 4'
                bat 'python hello-world.py'
            }
        }
    }
}
