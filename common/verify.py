# 依赖包
import re


def order_id(string):
    try:
        pattern = r"^\d{10}$"
        if re.match(pattern, string, flags=0):
            return True
        return False
    except:
        return False


def is_token(request):
    if request.method == 'POST':
        try:
            pattern = r"^\d{64}$"
            token = request.POST['token']
            if re.match(pattern, token, flags=0):
                return token
            return None
        except:
            return None
    elif request.method == 'GET':
        try:
            pattern = r"^\d{64}$"
            token = request.POST['token']
            if re.match(pattern, token, flags=0):
                return token
            return None
        except:
            return None
    else:
        return None


def is_order_id(request):
    if request.method == 'POST':
        try:
            pattern = r"^\d{32}$"
            order_id = request.POST['order_id']
            re_match = re.match(pattern, order_id, flags=0)
            if re_match:
                return order_id
            return None
        except:
            return None
    if request.method == 'GET':
        try:
            pattern = r"^\d{32}$"
            order_id = request.GET['order_id']
            re_match = re.match(pattern, order_id, flags=0)
            if re_match:
                return order_id
            return None
        except:
            return None


def is_glass_id(request):
    if request.method == 'POST':
        try:
            pattern = r"^\d{32}$"
            glass_id = request.POST['id']
            re_match = re.match(pattern, glass_id, flags=0)
            if re_match:
                return glass_id
        except Exception as msg:
            print(msg)
        return None
    elif request.method == 'GET':
        try:
            pattern = r"^\d{32}$"
            glass_id = request.GET['id']
            re_match = re.match(pattern, glass_id, flags=0)
            if re_match:
                return glass_id
        except Exception as msg:
            print(msg)
        return None
    else:
        return None


def is_phone(request):
    if request.method == 'POST':
        try:
            pattern = r"^\d{11}$"
            phone = request.POST['search']
            re_match = re.match(pattern, phone, flags=0)
            if re_match:
                return phone
            else:
                return None
        except:
            return None
    elif request.method == 'GET':
        try:
            pattern = r"^\d{11}$"
            phone = request.GET['search']
            re_match = re.match(pattern, phone, flags=0)
            if re_match:
                return phone
            else:
                return None
        except:
            return None


def is_int(string):
    """
    判读content值是否为正整数
    如果content值为正整数返回content值
    如果content值非正整数返回0
    """
    try:
        pattern = r"^[0-9]\d*$"
        re_match = re.match(pattern, string, flags=0)
        if re_match:
            return int(string)
        else:
            return 0
    except BaseException as msg:
        print("error", msg)
        return 0


def verify_id_get(request):
    """
    判断请求是否为 GET
    判断user_id 是否存在
    判断user_id 是否为16位纯数字
    """
    if request.method == 'GET':
        try:
            pattern = r"^\d{16}$"
            user_id = request.GET['user_id']
            re_match = re.match(pattern, user_id, flags=0)
            if re_match:
                return user_id
            else:
                return None
        except BaseException as msg:
            print(msg)
            return None
    else:
        return None


def verify_store_id(store_id):
    try:
        pattern = r"^\d{32}$"
        user_id = store_id
        re_match = re.match(pattern, user_id, flags=0)
        if re_match:
            return user_id
        else:
            return None
    except BaseException as msg:
        print(msg)
        return None


def verify_store_id_get(request):
    """
    判断请求是否为 GET
    判断user_id 是否存在
    判断user_id 是否为16位纯数字
    """
    if request.method == 'GET':
        try:
            pattern = r"^\d{32}$"
            user_id = request.GET['store_id']
            re_match = re.match(pattern, user_id, flags=0)
            if re_match:
                return user_id
            else:
                return None
        except BaseException as msg:
            print(msg)
            return None
    else:
        return None


def verify_order_id_get(request):
    if request.method == 'GET':
        try:
            order_id = request.GET['order_id']
        except:
            return None
        if order_id:
            pattern = r"^\d{32}$"
            re_match = re.match(pattern, order_id, flags=0)
            if re_match:
                return order_id
    return None


def verify_order_token_get(request):
    if request.method == 'GET':
        try:
            order_token = request.GET['order_token']
        except:
            return None
        if order_token:
            pattern = r"^\d{32}$"
            re_match = re.match(pattern, order_token, flags=0)
            if re_match:
                return order_token
    return None


def verify_phone_get(request):
    if request.method == 'GET':
        try:
            pattern = r"^\d{11}$"
            phone = request.GET['search']
            re_match = re.match(pattern, phone, flags=0)
            if re_match:
                return phone
            else:
                return None
        except:
            return None
    else:
        return None
