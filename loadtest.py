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


# choices = ["http://127.0.0.1:8001/ping", "http://127.0.0.1:8001/spanned_request", "http://127.0.0.1:8001/exception", "http://127.0.0.1:8001/sleep", "http://127.0.0.1:8001/invalid", "http://127.0.0.1:8001/foobar"] #, "http://127.0.0.1:8002/ping", "http://127.0.0.1:8002/spanned_request", "http://127.0.0.1:8002/exception", "http://127.0.0.1:8002/sleep", "http://127.0.0.1:8002/invalid", "http://127.0.0.1:8002/foobar"]
choices = ["http://127.0.0.1:8001/controlled_error"]
# for i in range(100_000):
i = 0
while True:
    i += 1
    print(f"iteration {i}")
    url = random.choice(choices)
    time.sleep(random.uniform(0,0.01))
    TestThread(url).start()
