CREATE DATABASE IF NOT EXISTS data_airflow CHARACTER SET utf8 COLLATE utf8_unicode_ci;

CREATE USER IF NOT EXISTS 'airflow'@'localhost' IDENTIFIED BY 'A!rfl0w123';

GRANT ALL PRIVILEGES ON data_airflow.* TO 'airflow'@'localhost';

CREATE USER IF NOT EXISTS 'hubble-dev'@'localhost' IDENTIFIED BY 'V!per@67';

GRANT SELECT, SHOW VIEW ON data_airflow.* TO 'hubble-dev'@'localhost' IDENTIFIED BY 'V!per@67';
