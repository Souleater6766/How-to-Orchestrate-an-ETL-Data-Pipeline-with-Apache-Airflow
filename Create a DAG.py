#DAG (Directed Acyclic Graph)#is a collection of tasks with dependencies between them. #In this step, you need to create a DAG file that defines the tasks #and their dependencies.

#Create a Python file called etl_dag.py #in your Airflow home directory (the default #is ~/airflow/dags). Add the following code to define the DAG:




from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='ETL data pipeline',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='extract',
    bash_command='python /path/to/extract.py',
    dag=dag,
)

t2 = BashOperator(
    task_id='transform',
    bash_command='python /path/to/transform.py',
    dag=dag,
)

t3 = BashOperator(
    task_id='load',
    bash_command='python /path/to/load.py',
    dag=dag,
)

t1 >> t2 >> t3
