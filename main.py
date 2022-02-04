import threading
import requests
from datetime import datetime

i = 0

lock = threading.Lock()


def get_answer():
    global i
    now = datetime.now()
    print(now.strftime("%H:%M:%S"), "STARTED")
    URL = "http://localhost:4200"
    r = requests.get(url=URL)
    if r.content:
        i += 1
        now = datetime.now()
        print(now.strftime("%H:%M:%S"), "SUCСESS")
    return True


for i in range(0, 1000):
    try:
        lock.acquire()
        thread = threading.Thread(target=get_answer)
        thread.start()
    except Exception as e:
        break
    finally:
        lock.release()
