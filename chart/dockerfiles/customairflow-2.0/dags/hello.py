"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

# export AIRFLOW_VAR_FOO_BAZ='{"hello":"world"}'


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 2, 7),
    "email": ["sharad.mishra@indexexchange.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

COMMAND='echo setting variable hello;export AIRFLOW_VAR_FOO_BAZ={"hello":"world"}'

# def init():
#     foo = Variable.get("foo",deserialize_json=True)
#     # foo_json = Variable.get("foo_baz", deserialize_json=True)
#     # print("foo->"+foo)
#     print(foo)
    # print("foo_baz"+foo_json)


dag = DAG("hello", default_args=default_args, schedule_interval=timedelta(1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
# t1 = BashOperator(task_id="custom", bash_command=getTaskName, dag=dag)
# t1 = PythonOperator(task_id='init',
#     python_callable=init,
#     dag=dag)

t2 = BashOperator(task_id="sleep", bash_command="sleep 5", retries=3, dag=dag)

# t2.set_upstream(t1)

