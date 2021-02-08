
# Running Apache-Airflow 2.0 on kubernetes locally using minikube

**Table of contents**
- [Pre-requisite](#pre-requisite)
- [Start-minikube](#start-minikube)
- [Install-chart for airflow-2.0] (#chart-airflow-2.0)
- [Dashboard-minikube] (#dashboard-minikube)
- [Airflow-webui] (#airflow-webui)

## Pre-requisite
In order to run apache-airflow-2.0 locally on kubernetes, following pre-requisites needs to be installed
1. [Docker](https://docs.docker.com/get-docker/)
2. [Minikube](https://minikube.sigs.k8s.io/docs/start/)
3. [Helm](https://helm.sh/docs/intro/install/)

## Start-minikube
Once minikube is installed, start minikube. 
Please make sure docker has been allocated 4 cpus and 8GB of memory.
Start minikube with following command:
minikube start --cpus 4 --memory 8192

## Install-chart
helm install airflow . \
  --set images.airflow.repository=sharadmishra/airflowcustom \
  --set images.airflow.tag=2.0.1rc2 \
  --set webserver.defaultUser.enabled=true \
  --set webserver.defaultUser.role=Admin \
  --set webserver.defaultUser.username=airflow \
  --set webserver.defaultUser.firstName=abc \
  --set webserver.defaultUser.lastName=xyz \
  --set webserver.defaultUser.email=abc@xyz.com \
  --set webserver.defaultUser.password=airflow \
  --set executor=KubernetesExecutor \
  --namespace airflow

## Dashboard-minikube
Start minikube dashboard by following command:
minikube dashboard

## Airflow-webui
Airflow webui can be launched by running following command:
minikube service airflow-webserver --namespace airflow
