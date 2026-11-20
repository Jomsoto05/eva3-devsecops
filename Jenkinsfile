pipeline {
    agent any

    stages {
        stage('1. Construccion (Build)') {
            steps {
                echo 'Construyendo imagen Docker de la aplicacion...'
                sh 'docker build -t eva3-app:latest .'
            }
        }

        stage('2. Despliegue Temporal para Pruebas') {
            steps {
                echo 'Levantando contenedor en red devsecops-net...'
                sh '''
                    docker rm -f eva3-app-container || true
                    docker run -d --name eva3-app-container --network devsecops-net -p 5000:5000 eva3-app:latest
                    sleep 5
                '''
            }
        }

        stage('3. Pruebas de Seguridad (OWASP ZAP)') {
            steps {
                echo 'Ejecutando escaneo automatizado DAST con OWASP ZAP...'
                sh '''
                    docker run --rm --network devsecops-net -v $(pwd):/zap/wrk/:rw ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t http://eva3-app-container:5000 -r zap_report.html || true
                '''
            }
        }

        stage('4. Despliegue a Produccion') {
            steps {
                echo 'Aplicacion desplegada y activa en http://localhost:5000'
                sh 'docker ps --filter "name=eva3-app-container"'
            }
        }
    }
}