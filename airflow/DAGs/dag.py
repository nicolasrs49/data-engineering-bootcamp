from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook

default_args = {
    'owner' : 'airflow',
    'depends_on_past' : False,
    'start_date' : datetime(2024,1,1),
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 0,
    'retry_delay' : timedelta(minutes=5),
}

@dag(
    dag_id = 'postgres_to_snowflake',
    default_args = default_args,
    description = 'Carrega dados de forma incremental do Postgres para Snowflake.',
    schedule_interval = timedelta(days=1),
    catchup = False # Define se o airflow vai re-executar todas as execuções que por algum motivo ele não conseguiu executar
)

def postgres_to_snowflake_etl():
    table_names = ['veiculos','estados','cidades','concessionarias','vendedores','clientes', 'vendas']

    for table_name in table_names:
        @task(task_id=f'get_max_id_{table_name}') # esse decorador diz que a função abaixo está associada à TASK.
        def get_max_primary_key(table_name: str):
            with SnowflakeHook(snowflake_conn_id='snowflake').get_conn() as conn:
                with conn.cursor() as cursor:
                    query = f'SELECT MAX(id_{table_name}) FROM {table_name}'
                    cursor.execute(query)
                    max_id = cursor.fetchone()[0]
                    return max_id if max_id is not None else 0
        
        @task(task_id=f'load_data_{table_name}')
        def load_incremental_data(table_name:str,max_id:int):
            with PostgresHook(postgres_conn_id='postgres').get_conn() as pgconn:
                with pgconn.cursor() as pg_cursor:
                    primary_key = f'id_{table_name}'
                    
                    # Pega o nome das colunas
                    query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'"
                    pg_cursor.execute(query)
                    columns = [row[0] for row in pg_cursor.fetchall()]
                    columns_list_str = ', '.join(columns)
                    placeholders = ', '.join(['%s'] * len(columns)) # Isso monta o insert especial: INSERT INTO veiculos, vendas, estados... VALUES(%s, %s, %s, ...)

                    # verifica se existem novos dados testando se o id do postgres é maior (mais recente) que o id do snowflake
                    query = f"SELECT {columns_list_str} FROM {table_name} WHERE {primary_key} > {max_id}"
                    pg_cursor.execute(query)
                    rows = pg_cursor.fetchall()

                    # Monta o insert dos dados no snowflake
                    with SnowflakeHook(snowflake_conn_id='snowflake').get_conn() as sf_conn:
                        with sf_conn.cursor() as sf_cursor:
                            insert_query = f"INSERT INTO {table_name} ({columns_list_str}) VALUES ({placeholders})"
                            for row in rows:
                                sf_cursor.execute(insert_query, row)

        # executa as funções armazenando os resultados
        max_id = get_max_primary_key(table_name)
        load_incremental_data(table_name, max_id)

dag_postgres_to_snowflake_etl = postgres_to_snowflake_etl()