from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator  import PythonOperator

from datetime import datetime

from test_script import *
from my_client_test import call_api

from aws_requests_auth.aws_auth import AWSRequestsAuth

def print_return_val(**kwargs):
    #xcom_value = str(ti.xcom_pull(task_ids="run_task3"))
    task_instance = kwargs['task_instance']
    xcom_value = task_instance.xcom_pull(task_ids='run_task3') #{{ task_instance.xcom_pull(task_ids='run_task3', key='table_name') }}
    print (f"xcom_value = {xcom_value}")

def ssh_connect():
    pass

with DAG(
    dag_id='dag_test_1',
    start_date=datetime(2022, 5, 28),
    schedule_interval=None
) as dag:

    start_task = EmptyOperator(
        task_id='start'
    )

    run_task = PythonOperator(
        task_id = 'run_task'
        ,python_callable=my_func1
        ,retries = 1
        ,dag = dag
    )

    run_task3 = PythonOperator(
        task_id = 'run_task3'
        ,python_callable=my_func3
        ,retries = 1
        ,dag = dag
    )

    run_task4 = PythonOperator(
        task_id = 'run_task4'
        ,python_callable=print_return_val
        ,retries = 1
        ,dag = dag
    )

    end_task = EmptyOperator(
        task_id='end'
    )

start_task >> run_task
run_task >> run_task3
run_task3 >> run_task4
run_task4 >> end_task