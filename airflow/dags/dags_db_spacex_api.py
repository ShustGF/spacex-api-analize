"""DAG по работе с API SpaceX"""

import json
import logging
# import os

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
        "postgres_conn_id": "server_publicist",
    },
    dag=dag,
)

add_launches_values_to_table = PythonOperator(
    task_id="add_launches_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_launches,
        "url": f"{K.HOST}/launches",
        "postgres_conn_id": "server_publicist",
    },
    dag=dag,
)

add_capsules_values_to_table = PythonOperator(
    task_id="add_capsules_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_capsules,
        "url": f"{K.HOST}/capsules",
        "postgres_conn_id": "server_publicist",
    },
    dag=dag,
)

add_cores_values_to_table = PythonOperator(
    task_id="add_cores_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_cores,
        "url": f"{K.HOST}/cores",
        "postgres_conn_id": "server_publicist",
    },
    dag=dag,
)

add_crew_values_to_table = PythonOperator(
    task_id="add_crew_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_crew,
        "url": f"{K.HOST}/crew",
        "postgres_conn_id": "server_publicist",
    },
    dag=dag,
)

add_landpads_values_to_table = PythonOperator(
    task_id="add_landpads_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_landpads,
        "url": f"{K.HOST}/landpads",
        "postgres_conn_id": "server_publicist",
    },
    dag=dag,
)

add_launchpads_values_to_table = PythonOperator(
    task_id="add_launchpads_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_launchpads,
        "url": f"{K.HOST}/launchpads",
        "postgres_conn_id": "server_publicist",
    },
    dag=dag,
)

add_payload_values_to_table = PythonOperator(
    task_id="add_payload_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_payload,
        "url": f"{K.HOST}/payloads",
        "postgres_conn_id": "server_publicist",
    },
    dag=dag,
)

add_ships_values_to_table = PythonOperator(
    task_id="add_ships_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_ships,
        "url": f"{K.HOST}/ships",
        "postgres_conn_id": "server_publicist",
    },
    dag=dag,
)

add_rockets_values_to_table = PythonOperator(
    task_id="add_rockets_values_to_table",
    python_callable=load_data_to_db,
    op_kwargs={
        "function_class": u.get_rockets,
        "url": f"{K.HOST}/rockets",
        "postgres_conn_id": "server_publicist",
    },
    dag=dag,
)

check_db_connection = PostgresOperator(
    task_id="check_db_connection",
    postgres_conn_id="server_publicist",
    sql="""
      SELECT 1
    """,
    dag=dag,
)

# create_table_to_spub = PostgresOperator(
#     task_id="create_table_to_spub",
#     postgres_conn_id="server_publicist",
#     sql="sql/create_table.sql",
#     dag=dag,
# )

# create_publication_spub = PostgresOperator(
#     task_id="create_publication_spub",
#     postgres_conn_id="server_publicist",
#     sql="""
#         CREATE PUBLICATION db_pub FOR ALL TABLES;
#     """,
#     dag=dag,
# )

# create_slot_spub = PostgresOperator(
#     task_id="create_slot_spub",
#     postgres_conn_id="server_publicist",
#     sql="""
#         SELECT pg_create_logical_replication_slot('my_pub_slot', 'pgoutput');
#     """,
#     dag=dag,
# )

# create_table_to_sub = PostgresOperator(
#     task_id="create_table_to_sub",
#     postgres_conn_id="server_subscription",
#     sql="sql/create_table.sql",
#     dag=dag,
# )

# create_subscribe_sub = PostgresOperator(
#     task_id="create_subscribe_sub",
#     postgres_conn_id="server_subscription",
#     sql=f"""
#         CREATE SUBSCRIPTION db_test_sub
#                 CONNECTION 'host=server_publicist
#                             port=5432
#                             user={os.getenv("POSTGRES_SENDER_USER")}
#                             password={os.getenv("POSTGRES_SENDER_PASSWORD")}
#                             dbname={os.getenv("POSTGRES_SENDER_DB")}'
#                 PUBLICATION db_pub
#                 with (
#                     create_slot = false,
#                     enabled = false,
#                     slot_name = my_pub_slot
#                     );
#         ALTER SUBSCRIPTION db_test_sub ENABLE;

#     """,
#     dag=dag,
# )

(
    check_db_connection
    # >> create_table_to_spub
    # >> create_table_to_sub
    # >> create_publication_spub
    # >> create_slot_spub
    # >> create_subscribe_sub
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
