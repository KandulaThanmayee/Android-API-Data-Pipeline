from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'you',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='api_violation_pipeline',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    generate_input = BashOperator(
        task_id='generate_input',
        bash_command='python3 src/input_generators/animation.py'
    )

    start_producer = BashOperator(
        task_id='start_producer',
        bash_command='python3 src/log_producer.py &'
    )

    start_consumer = BashOperator(
        task_id='start_consumer',
        bash_command='python3 src/log_consumer.py &'
    )

    analyze_results = BashOperator(
        task_id='analyze_results',
        bash_command='python3 src/cs.py'
    )

    generate_input >> start_producer >> start_consumer >> analyze_results
