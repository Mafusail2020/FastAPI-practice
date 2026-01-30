import requests

# print(requests.post("http://0.0.0.0:8000/", params={"data": "SOME_DATA"}).json())

print(requests.get("http://0.0.0.0:8000/444").json())

print(requests.get("http://0.0.0.0:8000/list").json())


# POSTING PART
import json

data = {"new_id": 1}
data = json.dumps(data)

resp = requests.post("http://0.0.0.0:8000/create_id/", json={"new_id": 1, "is_admin": True})
print(resp.json())
# print(resp.json())


# PUT PART
resp = requests.put("http://0.0.0.0:8000/123", data=json.dumps({"new_id": 124124}))
