
# Running Apache-Airflow 2.0 on kubernetes locally using minikube

**Table of contents**
- [Pre-requisite](#pre-requisite)
- [Fork-repository](#fork-repository)
- [Build-airflow-2.0-docker-image](#build-airflow-2.0-docker-image)
- [Start-minikube](#start-minikube)
- [Install-chart for airflow-2.0](#chart-airflow-2.0)
- [Dashboard-minikube](#dashboard-minikube)
- [Airflow-webui](#airflow-webui)
- [References](#references)

## Pre-requisite
In order to run apache-airflow-2.0 locally on kubernetes, following pre-requisites needs to be installed
1. [Docker](https://docs.docker.com/get-docker/)
2. [Minikube](https://minikube.sigs.k8s.io/docs/start/)
3. [Helm](https://helm.sh/docs/intro/install/)

## Start-minikube
Once minikube is installed, start minikube. 
Please make sure docker has been allocated 4 cpus and 8GB of memory.
Start minikube with following command:
```
minikube start --cpus 4 --memory 8192
```

## Fork-repository
Clone repository to your local
```
git clone https://github.com/imsharadmishra/airflow-2.0.git
```

## Build-airflow-2.0-docker-image
I have built a custom airflow-2.0 image with basic tools e.g. procps, vim etc for investigating issues in container.
You can also built a custom image for your need, here is a very good document on how to built custom image:
 [Airflow-documentation](https://airflow.apache.org/docs/apache-airflow/stable/production-deployment.html)
```
cd airflow-2.0/chart/dockerfiles/customairflow-2.0
docker build -t airflowcustom:2.0.1rc2 .
```

## Install-chart for airflow-2.0
```
# Using Executor type as Kubernetes Executor
kubectl create namespace airflow
cd airflow-2.0/chart
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

# Using Executor type as Celery Executor
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
  --set executor=CeleryExecutor \
  --set workeres.replicas=2 \
  --namespace airflow
```

## Dashboard-minikube
Start minikube dashboard by following command:
```
minikube dashboard
```

## Airflow-webui
Airflow webui can be launched by running following command:
```
minikube service airflow-webserver --namespace airflow
username=airflow
password=airflow
```

## References
1. [Airflow-youtube](https://www.youtube.com/watch?v=wDr3Y7q2XoI)
2. [Airflow-summit-Presentation](https://airflowsummit.org/slides/h2-ProductionContainerImages.pdf)
3. [Airflow-documentation](https://airflow.apache.org/docs/apache-airflow/stable/production-deployment.html)
