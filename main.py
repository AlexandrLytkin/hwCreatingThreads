import threading
import time


def num(_a, _b):
    for i in range(_a, _b + 1):
        print(i)
        time.sleep(1)


def string(_st):
    for i in _st:
        print(i)
        time.sleep(1)


a, b = 1, 10
st = "abcdefghij"
thr_one = threading.Thread(target=num, args=(a, b,), name="thr-one")
thr_two = threading.Thread(target=string, args=(st,), name="thr-two")

thr_one.start()
thr_two.start()

thr_one.join()
thr_two.join()
