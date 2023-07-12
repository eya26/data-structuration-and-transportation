import sqlite3
from datetime import datetime, date, timedelta
import requests
from datetime import date
from time import mktime
from airflow.decorators import dag, task

@dag(
    start_date=datetime(2023, 1, 11),
    schedule_interval="0 1 * * *",
    catchup=False
)
def Assignment_hard():

    def to_seconds_since_epoch(input_date: str) -> int:
        return int(mktime(date.fromisoformat(input_date).timetuple()))

    BASE_URL = "https://opensky-network.org/api"

    @task
    def fetch_Flight_Data(ds=None) -> list:
        if ds is None:
            ds = date.today() - timedelta(days=7)
        one_day = ds + timedelta(days=1)
        params = {
            "airport": "LFPG",
            "begin": to_seconds_since_epoch(str(ds)),
            "end": to_seconds_since_epoch(str(one_day))
        }
        response = requests.get(f"{BASE_URL}/flights/departure", params=params)
        flightData = response.json()
        return flightData

    @task
    def store_Flight_Data(flights: list, ds=None) -> None:
        if ds is None:
            ds = date.today().isoformat()
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS flights (
            icao24 TEXT,
            firstSeen INTEGER,
            estDepartureAirport TEXT,
            lastSeen INTEGER,
            estArrivalAirport TEXT,
            callsign TEXT,
            estDepartureAirportHorizDistance INTEGER,
            estDepartureAirportVertDistance INTEGER,
            estArrivalAirportHorizDistance INTEGER,
            estArrivalAirportVertDistance INTEGER,
            departureAirportCandidatesCount INTEGER,
            arrivalAirportCandidatesCount INTEGER,
            ds TEXT
        )
        ''')

        for flight in flights:
            cursor.execute(
                '''INSERT INTO flights (icao24, firstSeen, estDepartureAirport, lastSeen, estArrivalAirport, callsign, estDepartureAirportHorizDistance, estDepartureAirportVertDistance, estArrivalAirportHorizDistance, estArrivalAirportVertDistance, departureAirportCandidatesCount, arrivalAirportCandidatesCount, ds) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (flight['icao24'], flight['firstSeen'], flight['estDepartureAirport'], flight['lastSeen'],
                 flight['estArrivalAirport'], flight['callsign'], flight['estDepartureAirportHorizDistance'],
                 flight['estDepartureAirportVertDistance'], flight['estArrivalAirportHorizDistance'],
                 flight['estArrivalAirportVertDistance'], flight['departureAirportCandidatesCount'],
                 flight['arrivalAirportCandidatesCount'], ds))
        conn.commit()

        cursor.execute("SELECT * FROM flights")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.execute('''DROP TABLE flights''')
        conn.close()

    ds = date.today() - timedelta(days=7)
    flights = fetch_Flight_Data(ds=ds)
    store_Flight_Data(flights=flights, ds=ds.isoformat())


_ = Assignment_hard()
