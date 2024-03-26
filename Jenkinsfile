node {
  stage('SCM') {
    git 'https://github.com/robbiebise/launchpad'
  }
  stage('SonarQube analysis') {
    def scannerHome = tool 'sonar-scanner-cli'; // must match the name of an actual scanner installation directory on your Jenkins build agent
    withSonarQubeEnv('SonarCloud') { 
      sh "${scannerHome}/sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner"
    }
  }
}