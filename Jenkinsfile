pipeline {
	agent any
	stages {
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
