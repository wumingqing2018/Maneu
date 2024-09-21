from maneu.models import ManeuAdmin


def find_user_username(username=''):
    """
    通过username查找用户
    """
    return ManeuAdmin.objects.filter(username=username).first()


def sendsms(call='', code=''):
    return ManeuAdmin.objects.filter(phone=call).update(password=code)


def admin_login(call='', code=''):
    return ManeuAdmin.objects.filter(phone=call, password=code).first()