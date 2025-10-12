pipipeline{

    agent any
    environment {

        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        AWS_DEFAULT_REGION = 'eu-west-2'
    }
    parameters {

        
        
        choice choices: ['apply', 'destroy'], description: '''Choose your terraform action
        ''', name: 'action'
    }
    stages{


        stage("GitHub checkout....") {

            steps {

                script {

 
                    git branch: 'master', url: 'https://github.com/clement2019/python_flask_app.git' 
                }
            }
        }
        stage("Build docker connecting....."){

            steps{

                sh 'printenv'
                sh 'git version'
                sh 'docker build . -t good777lord/f-app2'
            }
        }
        stage("push image to DockerHub"){


            steps{


                script {
                    withCredentials([string(credentialsId: 'DOCKERID', variable: 'DOCKERID')]) {
                        sh 'docker login -u good777lord -p ${DOCKERID}'
                    }
                        sh 'docker push good777lord/f-app2:latest'
                }
            }
        }
        stage('Initializing teraform'){
            steps{
                script{
                    dir('terraform'){

                         sh 'terraform init'
                        
                    }
                }
            }
        }
        stage('Validating Terraform'){
            steps{

                script{

                    dir('terraform'){

                        sh 'terraform validate'
                    }
                }
            }
        }
        stage('Previewing the infrastructure'){
            steps{

                script{

                    dir('terraform'){

                        sh 'terraform plan'
                    }
                    input(message: "Approve?", ok: "proceed")
                }
            }
        }

        stage('Terraform Apply') {
            steps {
               
                script {
                    if (params.'action' == 'apply') {

                        echo "You have chosen to ${params.'action'} the resources"
                        dir('terraform'){
                            sh 'terraform $action --auto-approve'
                            sh 'aws eks describe-cluster --name my-eks-cluster1 --region eu-west-2'
                            sh ('aws eks update-kubeconfig --name my-eks-cluster1 --region eu-west-2')
                            
                            sh "kubectl apply -f aap-deployment.yaml"
                            //sh "kubectl apply -f service.yaml"
                                
                    
                        }
                    }
                }
        

            }
        }
       
        stage('Terraform Destroy') {
            steps {
               
                script {
                    if (params.'action' == 'destroy') {

                        echo "You have chosen to ${params.'action'} the resources"
                        dir('terraform'){
                            sh 'terraform $action --auto-approve'
                        
                        }
                    }
                }
        

            }
        }
    }
}
    