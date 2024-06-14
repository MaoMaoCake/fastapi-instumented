import os

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


endpoint_url = os.getenv("ENDPOINT_URL", "http://127.0.0.1:8001")

choices = [f"{endpoint_url}/ping", f"{endpoint_url}/spanned_request", f"{endpoint_url}/exception",
           f"{endpoint_url}/sleep",
           f"{endpoint_url}/invalid",
           f"{endpoint_url}/foobar"]  #, "http://127.0.0.1:8002/ping", "http://127.0.0.1:8002/spanned_request", "http://127.0.0.1:8002/exception", "http://127.0.0.1:8002/sleep", "http://127.0.0.1:8002/invalid", "http://127.0.0.1:8002/foobar"]
i = 0
while True:
    i += 1
    print(f"iteration {i}")
    url = random.choice(choices)
    time.sleep(random.uniform(0, float(os.getenv("REQUEST_RATE",0.01))))
    TestThread(url).start()
