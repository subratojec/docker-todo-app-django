pipeline {
    agent any
    stages {
        stage('checkout the code') {
            steps {
                git branch: 'main', url: 'https://github.com/sohitdeveloper/docker-todo-app-django.git'
            }
        }
        stage('build backend image') {
            steps {
                echo "building backend image started"
                sh 'docker build -t todo-be .'
                echo "building backend image completed"
            }
        }
        stage('login and push docker image') {
            steps {
                echo "login and push docker images"
                withCredentials([usernamePassword(credentialsId:"fd1e1861-03c9-4beb-85e1-803023e0fece", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: "DOCKER_USER")]) {
                    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASSWORD'
                    echo "login successfully"
                    
                    sh 'docker tag todo-be sohit28/todo-be'
                    sh "docker push sohit28/todo-be"
                    echo "Image pushed successfully"
                }
            }
        }
    }
}
