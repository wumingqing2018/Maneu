from maneu.models import ManeuAdmin


def find_user_username(username=''):
    """
    通过username查找用户
    """
    return ManeuAdmin.objects.filter(username=username).first()

def sendsms(phone='', password=''):
    return ManeuAdmin.objects.filter(phone=phone).update(password=password)
