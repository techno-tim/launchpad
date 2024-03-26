node {
  stage('SCM') {
    git 'https://github.com/robbiebise/launchpad'
  }
  stage('SonarQube analysis') {
    def scannerHome = tool 'sonar-scanner-cli'; // must match the name of an actual scanner installation directory on your Jenkins build agent
    withSonarQubeEnv('SonarCloud') { 
      sh "${scannerHome}/sonar-scanner-cli-5.0.1.3006-macosx/bin/sonar-scanner"
    }
  }
}