import requests
import random


choices = ["http://127.0.0.1:8001", "http://127.0.0.1:8002", "http://127.0.0.1:8003", "http://127.0.0.1:8004"]
for i in range(100000):
    print(f"iteration {i}")
    url = random.choice(choices)
    r = requests.get(url, verify=False)