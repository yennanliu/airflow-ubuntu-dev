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

def push_var(**kwargs):
    resp_dict = my_func2()
    task_instance = kwargs['task_instance']
    task_instance.xcom_push(key="key1", value=resp_dict["key1"])
    task_instance.xcom_push(key="key2", value=resp_dict["key2"])


with DAG(
    dag_id='dag_test_3',
    start_date=datetime(2022, 5, 28),
    schedule_interval=None
) as dag:

    start_task = EmptyOperator(
        task_id='start'
    )

    push_var = PythonOperator(
        task_id="push_var",
        python_callable=push_var,
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
        ,python_callable=my_func6
        #,op_kwargs={"input": "xxx"}
        #, op_kwargs={"input": "{{ ti.xcom_pull(task_ids='run_task3') }}"}
        ,op_kwargs={"input1": "{{ task_instance.xcom_pull(key='key1', task_ids='push_var') }}", "input2": "{{ task_instance.xcom_pull(key='key2', task_ids='push_var') }}"}
        ,retries = 1
        ,dag = dag
    )

    end_task = EmptyOperator(
        task_id='end'
    )

# start_task >> run_task3
# run_task3 >> my_func5
# my_func5 >> end_task

start_task >> push_var
push_var >> my_func5
my_func5 >> end_task