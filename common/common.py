# 依赖包
import datetime
import random
import time
import calendar

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

def day():
    """
    返回今天日期
    格式: Y-M-D
    """
    return time.strftime("%d", time.localtime())

def month():
    """
    返回今天日期
    格式: Y-M-D
    """
    now_time = datetime.datetime.now()  # 如果数据库保存的是UTC时间,程序不会蹦但是会提示你这不是本地时间

    return now_time.month

def year():
    """
    返回今天日期
    格式: Y-M-D
    """
    return time.strftime("%Y", time.localtime())


def yesterday(days):
    now = datetime.date.today()
    timedelta = datetime.timedelta(days=days)
    return now - timedelta


def create_id():
    """
    生成32位纯数字id
    """
    order = random.randint(10000000000000000000000000000000, 99999999999999999999999999999999)
    return order


def token():
    """
    生成32位纯数字token
    """
    rand_int = random.randint(10000000000000000000000000000000, 99999999999999999999999999999999)
    return rand_int


def make_qrcode(order_id, order_token):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )  # 设置二维码的大小
    url = f'http://maneu.online/guess/?order_id={order_id}&order_token={order_token}'
    qr.add_data(url)
    qr.make(fit=True)
    return qr


def res():
    """
    约束返回json格式
    code: 状态代码
    date: 信息内容
    msg: 返回信息
    """
    return {'code': '', 'msg': '', 'data': {}}


def get_ip(request):
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        return request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        return request.META.get("REMOTE_ADDR")


def daycount():
    time.strftime("%Y-%m-", time.localtime())
    monthRange = calendar.monthrange(year=int(year()), month=int(month()))
    return monthRange
