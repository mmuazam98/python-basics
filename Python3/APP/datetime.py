import threading
import datetime
import time


def thrd_1time():
    print("\nstarting thread 1")
    for _ in range(3):
        now = datetime.datetime.now()
        print("\nThread-1: " + now.strftime("%a %b %d %H:%M:%S %Y"))
        time.sleep(1)
    print("\nexit thread 1")


def thrd_2time():
    print("\nstarting thread 2")
    for _ in range(3):
        now = datetime.datetime.now()
        print("\nThread-2: " + now.strftime("%a %b %d %H:%M:%S %Y"))
        time.sleep(1)
    print("\nexit thread 2")


t1 = threading.Thread(target=thrd_1time)
t2 = threading.Thread(target=thrd_2time)
t1.start()
t2.start()
print("\nexiting main thread")
