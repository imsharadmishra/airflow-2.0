use data_airflow;
alter table `task_instance` change `execution_date` `execution_date` TIMESTAMP(6) not null DEFAULT CURRENT_TIMESTAMP(6);
