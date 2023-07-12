import requests
url = "https://opensky-network.org/api/flights/departure"
airport = "LFPG" 
date = "2022-12-01"

params = {
    "airport": airport,
    "date": date
}
response = requests.get(url, params=params)
