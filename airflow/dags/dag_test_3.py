from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator  import PythonOperator
from airflow.contrib.operators.ssh_operator  import SSHOperator

from datetime import datetime

from test_script import *
from my_client_test import call_api

ssh_command="echo 123"

def print_return_val(**kwargs):
    task_instance = kwargs['task_instance']
    xcom_value = task_instance.xcom_pull(task_ids='run_task3') #{{ task_instance.xcom_pull(task_ids='run_task3', key='table_name') }}
    print (f"xcom_value = {xcom_value}")

def hello_world(ti, execution_date, **context):
    print("Hello World")
    return "Gorgeous"


with DAG(
    dag_id='dag_test_3',
    start_date=datetime(2022, 5, 28),
    schedule_interval=None
) as dag:

    start_task = EmptyOperator(
        task_id='start'
    )

    my_func2 = PythonOperator(
        task_id="my_func2",
        python_callable=my_func2,
    )

    # run_task3 = PythonOperator(
    #     task_id = 'run_task_3'
    #     ,python_callable=my_func3
    #     ,retries = 1
    #     ,dag = dag
    # )

    my_func5 = PythonOperator(
        task_id = 'my_func5'
        #,python_callable=print_return_val
        ,python_callable=my_func5
        #,op_kwargs={"input": "xxx"}
        #, op_kwargs={"input": "{{ ti.xcom_pull(task_ids='run_task3') }}"}
        ,op_kwargs={"input": my_func2.output}
        ,retries = 1
        ,dag = dag
    )

    end_task = EmptyOperator(
        task_id='end'
    )

# start_task >> run_task3
# run_task3 >> my_func5
# my_func5 >> end_task

start_task >> my_func2
my_func2 >> my_func5
my_func5 >> end_task