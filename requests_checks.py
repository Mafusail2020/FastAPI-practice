import requests

print(requests.post("http://0.0.0.0:8000/", params={"data": "SOME_DATA"}).json())

print(requests.get("http://0.0.0.0:8000/444").json())
