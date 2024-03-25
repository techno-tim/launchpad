node {
  stage('Preparation') {
    // Check if Node.js is installed
    sh 'node --version || echo "Node.js is not installed"'
    // Install Node.js if not installed
    sh 'which node || curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && . ~/.nvm/nvm.sh && nvm install node'
  }
  stage('SCM') {
    git 'https://github.com/robbiebise/launchpad'
  }
  stage('SonarQube analysis') {
    def scannerHome = tool 'Sonar Scanner Global'; // must match the name of an actual scanner installation directory on your Jenkins build agent
    withSonarQubeEnv('SonarCloud') { 
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}