pipeline {
    agent any
    stages {
        stage('start') {
            steps {
                echo 'Start Stage'
				git 'https://github.com/mohammed-anka/Python_Jenkins_UnitTest_Demo.git'
            }
        }
		stage('build') {
            steps {
                echo 'Build Stage'
				sh 'python hello.py'
            }
        }
		stage('test') {
            steps {
                echo 'Test Stage'
				sh 'python hello_test.py'
            }
        }
    }
    post { 
        always { 
            echo 'I will always say Hello again!'
        }
    }
}