#!/bin/bash
mysql -uroot -proot -P3306 < /tmp/create_user_db.sql
mysql -uairflow -p'A!rfl0w123' < /tmp/data_airflow.sql
mysql -uroot -proot -P3306 < /tmp/update_tables.sql
# airflow db init
