node {
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
