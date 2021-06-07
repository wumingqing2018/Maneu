# 依赖包
import time
import random


def current_time():
    """
    返回当前时间
    格式: Y-M-D H:M:S
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def today():
    """
    返回今天日期
    格式: Y-M-D
    """
    return time.strftime("%Y-%m-%d", time.localtime())


def create_id():
    """
    生成32位纯数字订单编号
    """
    rand_int = random.randint(10000000000000000000000000000000,
                              99999999999999999999999999999999)
    return str(rand_int)


def token():
    """
    生成64位纯数字token
    """
    rand_int = random.randint(10000000000000000000000000000000,
                              99999999999999999999999999999999)
    return rand_int


def qrcode(order_id, token):
    print(order_id, token)
    return None


def res():
    return {'code': '', 'msg': '', 'data': {}}
