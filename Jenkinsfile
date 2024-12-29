pipeline {
    agent any

    parameters {
        choice(name: 'BRANCH_NAME', choices: ['dev', 'fhml', 'prod'], description: 'Select environment branch')
        choice(name: 'MODEL_NAME', choices: ['sql', 'notebook', 'snowspark'], description: 'Select model type')
    }

    environment {
        SNOWFLAKE_USER = credentials('SNOWFLAKE_USER')
        SNOWFLAKE_PASSWORD = credentials('SNOWFLAKE_PASSWORD')
        SNOWFLAKE_ACCOUNT = credentials('SNOWFLAKE_ACCOUNT')
        MAVEN_HOME = 'C:/Program Files/Apache Software Foundation/apache-maven-3.8.6'   // Adjust Maven path
        JAVA_HOME = 'C:/Program Files/Java/jdk-17'     // Adjust Java path
        SCALA_HOME = 'C:/Program Files (x86)/scala'   // Adjust Scala path
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "*/${params.BRANCH_NAME}"]],
                          userRemoteConfigs: [[url: 'https://github.com/manjunathbabur/dev_poc_project.git']]])
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    if (params.MODEL_NAME == 'sql') {
                        echo "Running SQL Tests..."
                        sh 'python3 -m pytest tests/sql_tests.py'
                    } else if (params.MODEL_NAME == 'notebook') {
                        echo "Running Notebook Tests..."
                        sh 'python3 -m pytest tests/notebook_tests.py'
                    } else if (params.MODEL_NAME == 'snowspark') {
                        echo "Running Snowpark Tests..."
                        sh '${MAVEN_HOME}/bin/mvn test'
                    }
                }
            }
        }

        stage('Build (for Snowpark only)') {
            when {
                expression { params.MODEL_NAME == 'snowspark' }
            }
            steps {
                sh '${MAVEN_HOME}/bin/mvn clean compile'
            }
        }

        stage('Package (for Snowpark only)') {
            when {
                expression { params.MODEL_NAME == 'snowspark' }
            }
            steps {
                sh '${MAVEN_HOME}/bin/mvn package'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (params.MODEL_NAME == 'sql') {
                        echo "Deploying SQL Scripts..."
                        sh '''
                        snowsql -a $SNOWFLAKE_ACCOUNT -u $SNOWFLAKE_USER -p $SNOWFLAKE_PASSWORD -f sql/deploy.sql
                        '''
                    } else if (params.MODEL_NAME == 'notebook') {
                        echo "Deploying Notebook..."
                        sh '''
                        snowsql -a $SNOWFLAKE_ACCOUNT -u $SNOWFLAKE_USER -p $SNOWFLAKE_PASSWORD -f notebooks/deploy.sql
                        '''
                    } else if (params.MODEL_NAME == 'snowspark') {
                        echo "Deploying Snowpark Application..."
                        sh 'java -jar target/snowpark-scala-app-1.0-SNAPSHOT.jar'
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully for ${params.MODEL_NAME} in ${params.BRANCH_NAME}!"
        }
        failure {
            echo "Pipeline failed for ${params.MODEL_NAME} in ${params.BRANCH_NAME}."
        }
    }
}
