from collections import Counter
from datetime import date
from time import mktime
import json
from dataclasses import dataclass
from datetime import datetime
import requests
from typing import List
from airflow.decorators import dag, task
from airflow.utils.dates import datetime

@dag(
    schedule_interval='0 1 * * *',  
    start_date=datetime(2023, 1, 12),
    catchup=False
)
def DST_Assignment_Easy():

    def to_seconds_since_epoch(input_date: str) -> int:
        return int(mktime(date.fromisoformat(input_date).timetuple()))

    @task
    def Reads_flights_leaving_CDG() -> dict:
        BASE_URL = "https://opensky-network.org/api"

        params = {
            "airport": "LFPG",  # ICAO code for CDG
            "begin": to_seconds_since_epoch("2022-12-01"),
            "end": to_seconds_since_epoch("2022-12-02")
        }

        cdg_flights = f"{BASE_URL}/flights/departure"
        response = requests.get(cdg_flights, params=params).text

        return {"response": response}

    @task
    def write_to_JSON(flights: dict):
        flights_data = json.loads(flights["response"])
        return {"flights": flights_data}
    
    response = Reads_flights_leaving_CDG()
    result = write_to_JSON(response)

DST_Assignment = DST_Assignment_Easy()
