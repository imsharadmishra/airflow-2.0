FROM mysql:5.7
ENV DEBIAN_FRONTEND noninteractive

USER root
# COPY requirements.txt /tmp/requirements.txt
RUN apt update -y
RUN apt-get install -y --no-install-recommends \
	python3-setuptools \
        freetds-bin \
        krb5-user \
        ldap-utils \
        libffi6 \
        libsasl2-2 \
        libsasl2-modules \
        libssl1.1 \
        locales  \
        lsb-release \
        sasl2-bin \
        sqlite3 \
        unixodbc \
        vim \
        procps \
        python3.7 \
        python3-pip \
        python3-dev default-libmysqlclient-dev build-essential
RUN pip3 install --upgrade pip
ARG AIRFLOW_VERSION=2.0.1
ARG PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.7.txt"
RUN echo $AIRFLOW_VERSION $PYTHON_VERSION $CONSTRAINT_URL
RUN pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
RUN pip3 install PyMySQL mysqlclient
RUN airflow;exit 0
COPY airflow.cfg /tmp/airflow.cfg
COPY create_db.sh /docker-entrypoint-initdb.d/z_create_db.sh
# COPY create_db.sh /tmp/z_create_db.sh
COPY create_user_db.sql /tmp/create_user_db.sql
COPY data_airflow.sql /tmp/data_airflow.sql
COPY update_tables.sql /tmp/update_tables.sql
RUN cp /tmp/airflow.cfg /root/airflow/airflow.cfg
RUN chmod +x /docker-entrypoint-initdb.d/z_create_db.sh
# ENTRYPOINT ["/bin/bash","/tmp/create_db.sh"]
