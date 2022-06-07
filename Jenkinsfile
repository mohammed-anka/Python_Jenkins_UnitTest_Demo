pipeline {
	agent any
	stages {
		stage("start") {
			steps {
				echo 'starting the application'
				git branch: 'main', url: 'https://github.com/mohammed-anka/Python_Jenkins_UnitTest_Demo.git'
			}
		}
		stage("build") {
			steps {
				echo 'building the application'
				bat "python hello.py"
			}
		}
		stage("test") {
			steps {
				echo "Testing the apk..."
				bat "python hello_test.py"
			}
		}
		stage("deploy") {
			steps {
				echo "Deploy ...."
			}
		}
	}
}
