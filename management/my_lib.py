import time
import random

def current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def current_day():
    return time.strftime("%Y-%m-%d", time.localtime())


def creste_order_id():
    rand_int = random.randint(10, 99)
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    item = now_time + str(rand_int)
    return item