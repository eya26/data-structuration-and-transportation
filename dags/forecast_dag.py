from airflow.decorators import dag, task
from datetime import datetime
from weather import get_forecast, transform_data, write_to_file


@dag(
    dag_id='exam_dag',
    schedule_interval="0 1 * * *",
    start_date=datetime(2023, 2, 5),
    catchup=False,
)
def exam_dag():
    @task(multiple_outputs=True)
    def get_weather(lat: float, lng: float, ds=None) -> dict:
        forecast_data = get_forecast(lat, lng, ds)
        return {"forecast_data": forecast_data}

    @task(multiple_outputs=True)
    def transform_forecast_data(data: dict) -> dict:
        trans_data = transform_data(data["forecast_data"])
        return {"trans_data": trans_data}

    @task
    def write(data: dict) -> None:
        write_to_file(data)

    latitude = 0.52
    longitude = 1.41

    data = get_weather(latitude, longitude)
    trans_data = transform_forecast_data(data)
    write(trans_data)


_ = exam_dag()
