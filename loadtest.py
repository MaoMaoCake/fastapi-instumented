import requests
import random
import threading
import time

exitFlag = 0


class TestThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        requests.get(self.url, verify=False)


choices = ["http://127.0.0.1:8001", "http://127.0.0.1:8002", "http://127.0.0.1:8003", "http://127.0.0.1:8004",
           "http://127.0.0.1:8010", "http://127.0.0.1:8011", "http://127.0.0.1:8012", "http://127.0.0.1:8013",
           "http://127.0.0.1:8014"]
for i in range(100000):
    print(f"iteration {i}")
    url = random.choice(choices)
    TestThread(url).start()
