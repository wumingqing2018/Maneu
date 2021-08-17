# 依赖包
import random
import time
import qrcode


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
    生成32位纯数字id
    """
    rand_int = random.randint(10000000000000000000000000000000,
                              99999999999999999999999999999999)
    return str(rand_int)


def token():
    """
    生成32位纯数字token
    """
    rand_int = random.randint(10000000000000000000000000000000,
                              99999999999999999999999999999999)
    return str(rand_int)


def make_qrcode(order_id, order_token):
    print(order_id, order_token)
    return None


def res():
    """
    约束返回json格式
    code: 状态代码
    date: 信息内容
    msg: 返回信息
    """
    return {'code': '', 'msg': '', 'data': {}}
