import threading
import time

def define_func():
    print("ran")
    time.sleep(1)
    print("done")

x = threading.Thread(target=define_func, args=())

x.start()

print(threading.active_count())