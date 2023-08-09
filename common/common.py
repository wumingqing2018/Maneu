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


def index_time(request):
    if request.GET.get('time'):
        time = request.GET.get('time')
    else:
        time = today()
    date = datetime.datetime.strptime(time, '%Y-%m-%d')
    down_day = (date + datetime.timedelta(days=+1)).strftime("%Y-%m-%d")
    up_day = (date + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    return {'list': '', 'time': time, 'up_day': up_day, 'down_day': down_day}


def subjective_content(request):
    content = {'OD_VA': request.POST['OD_VA'], 'OD_SPH': request.POST['OD_SPH'], 'OD_CYL': request.POST['OD_CYL'],
               'OD_AX': request.POST['OD_AX'], 'OD_ADD': request.POST['OD_ADD'], 'OD_BCVA': request.POST['OD_BCVA'],
               'OD_AL': request.POST['OD_AL'], 'OD_AK': request.POST['OD_AK'], 'OD_AD': request.POST['OD_AD'],
               'OD_CCT': request.POST['OD_CCT'], 'OD_LT': request.POST['OD_LT'], 'OD_VT': request.POST['OD_VT'],
               'OS_VA': request.POST['OS_VA'], 'OS_SPH': request.POST['OS_SPH'], 'OS_CYL': request.POST['OS_CYL'],
               'OS_AX': request.POST['OS_AX'], 'OS_ADD': request.POST['OS_ADD'], 'OS_BCVA': request.POST['OS_BCVA'],
               'OS_AL': request.POST['OS_AL'], 'OS_AK': request.POST['OS_AK'], 'OS_AD': request.POST['OS_AD'],
               'OS_CCT': request.POST['OS_CCT'], 'OS_LT': request.POST['OS_LT'], 'OS_VT': request.POST['OS_VT']}
    return content
