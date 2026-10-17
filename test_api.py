import requests

BASE = "http://127.0.0.1:5000"
payload ={
    "id":2,
    "task":"math",
    "status":"pending",
    "dates":"2026-01-02"
}

response = requests.post(f"{BASE}/Add_task",json=payload)
print("Status Code:", response.status_code)
print("Response:", response.text)