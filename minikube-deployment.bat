@echo off
REM Start Minikube with default settings
echo Starting Minikube...
minikube start
timeout /t 5 /nobreak  REM Wait for 5 seconds to ensure Minikube starts

REM Check Minikube status
echo Checking Minikube status...
minikube status
timeout /t 5 /nobreak  REM Wait for 5 seconds to allow status check completion

REM Create Kubernetes Secret for SSL certificates
echo Creating Kubernetes Secret for SSL certificates...
kubectl create secret generic nginx-certs --from-file=nginx/certs/nginx-selfsigned.crt --from-file=nginx/certs/nginx-selfsigned.key
REM The secret 'nginx-certs' is created from the specified certificate and key files

REM Start Minikube tunnel to expose LoadBalancer services
echo Starting Minikube tunnel...
start cmd /k "minikube tunnel"  REM Open a new CMD window to run Minikube tunnel
timeout /t 5 /nobreak  REM Wait for 5 seconds to allow the tunnel to start

REM Deploy Kubernetes manifests for deployments and services
echo Deploying Kubernetes manifests...
kubectl apply -f k8s/flask-api-deployment.yaml
kubectl apply -f k8s/streamlit-ui-deployment.yaml
kubectl apply -f k8s/nginx-server-deployment.yaml
kubectl apply -f k8s/flask-api-service.yaml
kubectl apply -f k8s/streamlit-ui-service.yaml
kubectl apply -f k8s/nginx-server-service.yaml
REM Apply the specified Kubernetes manifests for deployments and services
timeout /t 5 /nobreak  REM Wait for 5 seconds to ensure deployments start

REM Wait for each deployment to become available
echo Waiting for Flask API deployment to become available...
kubectl wait --for=condition=available --timeout=90s deployment/flask-api

echo Waiting for Streamlit UI deployment to become available...
kubectl wait --for=condition=available --timeout=90s deployment/streamlit-ui

echo Waiting for Nginx deployment to become available...
kubectl wait --for=condition=available --timeout=90s deployment/nginx-server
REM Wait until each deployment is available with a timeout of 90 seconds

REM List services to verify deployments
echo Services in the cluster:
kubectl get services
REM List all services to verify that deployments are running correctly

REM Pause the script to keep the CMD window open for inspection
pause
