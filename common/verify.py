import time
from uuid import UUID
"""
通用校验工具
"""


def date_method_post(request):
    """判断是否是一个有效的日期字符串"""
    try:
        str_date = request.POST['content']
        if ":" in str_date:
            time.strptime(str_date, "%Y-%m-%d %H:%M:%S")
        else:
            time.strptime(str_date, "%Y-%m-%d")
        return str_date
    except BaseException as e:
        print(e)
        return None


def verifyUUid(str=''):
    try:
        UUID(str).version
        return True
    except:
        return False