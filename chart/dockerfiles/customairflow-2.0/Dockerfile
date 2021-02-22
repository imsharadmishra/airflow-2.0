FROM apache/airflow:2.0.1rc2-python3.8
USER root
RUN  apt-get update -y && apt-get install -y \
    procps \
    vim
RUN pip install apache-airflow-providers-apache-spark
COPY dags/ /opt/airflow/dags/
USER airflow
