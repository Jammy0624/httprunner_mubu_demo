import time
from httprunner.response import ResponseObject
from httprunner import __version__
import random

def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

#自定义函数
def custom_sleep(n_secs):
    time.sleep(n_secs)

def get_unreadCount(response:ResponseObject):
    resp_json = response.resp_obj.json()
    unreadCount = resp_json["data"]["unreadCount"]
    print(f'get_unreadCount {unreadCount}')
    return unreadCount

def get_random_title():
    r = random.randint(0,100000)
    return f'title-{r}'