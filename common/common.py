# 依赖包
import datetime
import time


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
    now_time = datetime.datetime.now()  # 如果数据库保存的是UTC时间,程序不会蹦但是会提示你这不是本地时间
    return now_time.day

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
    now_time = datetime.datetime.now()  # 如果数据库保存的是UTC时间,程序不会蹦但是会提示你这不是本地时间
    return now_time.year


def yesterday(days):
    now = datetime.date.today()
    timedelta = datetime.timedelta(days=days)
    return now - timedelta


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
