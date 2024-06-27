pipeline {
    agent any

    stages {
        stage('Step 1') {
            steps {
                echo 'Step 1'
                sh 'java -version'
            }
        }
        stage('Step 2') {
            steps {
                echo 'Step 2'
                sh 'git --version'
            }
        }
        stage('Cloning Repo') {
            steps {
                echo 'Step 3'
                git branch: 'graph_feature', url: 'https://github.com/suryatiru/Emphasis.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Step 4'
                sh 'python3 -V'
            }
        }
    }
}
