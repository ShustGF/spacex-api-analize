"""DAG по работе с API SpaceX"""

import json
import logging

import utils as u
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago
from sqlalchemy.orm import Session


# Класс с константами
class K:
    HOST = "https://api.spacexdata.com/v4"


def load_data_to_db(function_class, url, postgres_conn_id):
    pg_hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    engine = pg_hook.get_sqlalchemy_engine()
    session = Session(bind=engine)
    json_values = json.loads(u.get_data_from_url(url))
    session.add_all([function_class(json_value) for json_value in json_values])
    session.commit()
    logger.info(f"Данные от URL({url}) обработаны успешно")


logger = logging.getLogger(__name__)


dag = DAG(
    dag_id="dags_db_spacex_api",
    start_date=days_ago(5),
    schedule_interval=None,
)

add_starlink_values_to_table = PythonOperator(
    task_id="add_starlink_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_starlinks,
        "url": f"{K.HOST}/starlink",
        "postgres_conn_id": "logical_rep",
    },
    dag=dag,
)

add_launches_values_to_table = PythonOperator(
    task_id="add_launches_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_launches,
        "url": f"{K.HOST}/launches",
        "postgres_conn_id": "logical_rep",
    },
    dag=dag,
)

add_capsules_values_to_table = PythonOperator(
    task_id="add_capsules_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_capsules,
        "url": f"{K.HOST}/capsules",
        "postgres_conn_id": "logical_rep",
    },
    dag=dag,
)

add_cores_values_to_table = PythonOperator(
    task_id="add_cores_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_cores,
        "url": f"{K.HOST}/cores",
        "postgres_conn_id": "logical_rep",
    },
    dag=dag,
)

add_crew_values_to_table = PythonOperator(
    task_id="add_crew_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_crew,
        "url": f"{K.HOST}/crew",
        "postgres_conn_id": "logical_rep",
    },
    dag=dag,
)

add_landpads_values_to_table = PythonOperator(
    task_id="add_landpads_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_landpads,
        "url": f"{K.HOST}/landpads",
        "postgres_conn_id": "logical_rep",
    },
    dag=dag,
)

add_launchpads_values_to_table = PythonOperator(
    task_id="add_launchpads_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_launchpads,
        "url": f"{K.HOST}/launchpads",
        "postgres_conn_id": "logical_rep",
    },
    dag=dag,
)

add_payload_values_to_table = PythonOperator(
    task_id="add_payload_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_payload,
        "url": f"{K.HOST}/payloads",
        "postgres_conn_id": "logical_rep",
    },
    dag=dag,
)

add_ships_values_to_table = PythonOperator(
    task_id="add_ships_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_ships,
        "url": f"{K.HOST}/ships",
        "postgres_conn_id": "logical_rep",
    },
    dag=dag,
)

add_rockets_values_to_table = PythonOperator(
    task_id="add_rockets_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_rockets,
        "url": f"{K.HOST}/rockets",
        "postgres_conn_id": "logical_rep",
    },
    dag=dag,
)

check_db_connection = PostgresOperator(
    task_id="check_db_connection",
    postgres_conn_id="logical_rep",
    sql="""
      SELECT 1
    """,
    dag=dag,
)

(
    check_db_connection
    >> add_starlink_values_to_table
    >> add_launches_values_to_table
    >> add_capsules_values_to_table
    >> add_cores_values_to_table
    >> add_crew_values_to_table
    >> add_landpads_values_to_table
    >> add_launchpads_values_to_table
    >> add_payload_values_to_table
    >> add_ships_values_to_table
    >> add_rockets_values_to_table
)
