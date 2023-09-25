pipeline{
    agent any
    stages{
      
      stage('Compile and Clean'){
        steps{
        sh "mvn clean compile"
      }
    }
      
  stage('test'){
    steps{
      sh "mvn site"
    }
  }

  stage('Deploy'){
    steps{
      sh "mvn package"
    }
  }
  stage('Archving'){
    steps{
      archiveArtifacts '**/target/*.jar
    }
  }
}

}
