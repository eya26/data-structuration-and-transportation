from typing import List
import requests

def get_weather_data(area: str, date: str, weather_events: List[str]) -> dict:
    BASE_URL = "https://open-meteo.com/"  

    params = {
        "area": area,
        "date": date,
        "events": ",".join(weather_events)
    }

    response = requests.get(BASE_URL, params=params).json()

    return response

def calculate_average_temperature(weather_data: dict) -> float:
    temperatures = weather_data["temperatures"]
    total_temperatures = sum(temperatures)
    average_temperature = total_temperatures / len(temperatures)

    return average_temperature
