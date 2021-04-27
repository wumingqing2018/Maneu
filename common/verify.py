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


