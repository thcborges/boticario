from datetime import datetime
from airflow.decorators import dag, task

from boticario import (
    BaseIngestionTask,
    BaseTable1Task,
    BaseTable2Task,
    BaseTable3Task,
    BaseTable4Task,
    SpotifyDataHackersExtract50Task,
    SpotifyDataHackersExtractFullTask,
    SpotifyTable5Task,
    SpotifyTable6Task,
    SpotifyTable7Task,
)


@dag(schedule='@daily', start_date=datetime(2023, 3, 20), catchup=False)
def base_flow():
    @task(task_id='base_ingestion')
    def base_ingestion_task():
        return BaseIngestionTask().run()
    
    @task(task_id='base_tabela1')
    def base_table1_task():
        return BaseTable1Task().run()
    
    @task(task_id='base_tabela2')
    def base_table2_task():
        return BaseTable2Task().run()
    
    @task(task_id='base_tabela3')
    def base_table3_task():
        return BaseTable3Task().run()
    
    @task(task_id='base_tabela4')
    def base_table4_task():
        return BaseTable4Task().run()

    base_ingestion_task(
        [
            base_table1_task(),
            base_table2_task,
            base_table3_task,
            base_table4_task
        ]
    )

base_flow()
