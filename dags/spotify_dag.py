from datetime import datetime
from airflow.decorators import dag, task

from boticario import (
    SpotifyDataHackersExtract50Task,
    SpotifyDataHackersExtractFullTask,
    SpotifyTable5Task,
    SpotifyTable6Task,
    SpotifyTable7Task,
)


@dag(schedule='@daily', start_date=datetime(2023, 3, 20), catchup=False)
def spotify_flow():
    @task(task_id='extract_first_50_records_from_spotify')
    def extract_50():
        return SpotifyDataHackersExtract50Task().run()
    
    @task(task_id='spotfy_tabela5')
    def table5():
        return SpotifyTable5Task().run()
    
    @task(task_id='extract_all_data_hackers_episodes_from_spotify')
    def extract_all():
        return SpotifyDataHackersExtractFullTask().run()
    
    @task(task_id='spotify_tabela6')
    def table6():
        return SpotifyTable6Task().run()
    
    @task(task_id='spotify_tabela7')
    def table7():
        return SpotifyTable7Task().run()

    extract_50(table5())
    extract_all([table6(), table7()])

spotify_flow()
