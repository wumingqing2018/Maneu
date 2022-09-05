import re
"""
通用校验工具
"""


def is_int(string):
    """_summary_

    Args:
        string (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        re_match = re.match(r"^[0-9]\d*$", string, flags=0)
        if re_match:
            return int(string)
    except BaseException as msg:
        print("error", msg)
    return 0


def user_id_method_get(request):
    """
    判断请求是否为 GET
    判断user_id 是否存在
    判断user_id 是否为16位纯数字
    """
    if request.method == 'GET':
        try:
            user_id = request.GET['user_id']
            re_match = re.match(r"^\d{32}$", user_id, flags=0)
            if re_match:
                return user_id
        except BaseException as msg:
            print(msg)
    return None


def store_id_method_get(request):
    """
    判断请求是否为 GET
    判断user_id 是否存在
    判断user_id 是否为16位纯数字
    """
    if request.method == 'GET':
        try:
            user_id = request.GET['store_id']
            re_match = re.match(r"^\d{32}$", user_id, flags=0)
            if re_match:
                return user_id
        except BaseException as msg:
            print(msg)
    return None


def order_id_method_get(request):
    """
    检验GET请求的order_id是否为32位正整数
    """
    if request.method == 'GET':
        try:
            order_id = request.GET['order_id']
            if len(order_id) == 36:
                return order_id
        except Exception as msg:
            print(msg)
    return None


def order_id_method_post(request):
    if request.method == 'POST':
        try:
            order_id = request.POST['order_id']
            re_match = re.match(r"^\d{32}$", order_id, flags=0)
            if re_match:
                return order_id
        except Exception as msg:
            print(msg)
    return None


def order_token_method_get(request):
    if request.method == 'GET':
        try:
            order_token = request.GET['order_token']
            re_match = re.match(r"^\d{32}$", order_token, flags=0)
            if re_match:
                return order_token
        except Exception as msg:
            print(msg)
    return None


def order_token_method_post(request):
    if request.method == 'POST':
        try:
            order_token = request.POST['order_token']
            re_match = re.match(r"^\d{32}$", order_token, flags=0)
            if re_match:
                return order_token
        except Exception as msg:
            print(msg)
    return None


def phone_method_Post(request):
    if request.method == 'POST':
        try:
            phone = request.POST['phone']
            re_match = re.match(r"^\d{11}$", phone, flags=0)
            if re_match:
                return phone
        except Exception as msg:
            print(msg)
    return None
