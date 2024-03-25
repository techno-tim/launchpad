pipeline {
    agent {
        docker {
            image 'ubuntu:latest' // Use the latest Ubuntu Docker image
            args '-u root:root' // Run as root to avoid permission issues
        }
    }
    stages {
        stage('Preparation') {
            steps {
                // Install Node.js
                sh 'apt-get update && apt-get install -y nodejs'
                // Check if Node.js is installed
                sh 'node --version || echo "Node.js is not installed"'
            }
        }
        stage('SCM') {
            steps {
                git 'https://github.com/robbiebise/launchpad'
            }
        }
        stage('SonarQube analysis') {
            steps {
                def scannerHome = tool 'Sonar Scanner Global'; // must match the name of an actual scanner installation directory on your Jenkins build agent
                withSonarQubeEnv('SonarCloud') { 
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}