pipeline {
	agent any
	stages {
		stage("build") {
			steps {
				echo 'building the application'
				sh "python hello.py"
			}
		}
		stage("test") {
			steps {
				echo "Testing the apk..."
			}
		}
		stage("deploy") {
			steps {
				echo "Deploy ...."
			}
		}
	}
}
