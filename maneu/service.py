from maneu.models import ManeuUsers


def find_user_username(username=''):
    """
    通过username查找用户
    """
    return ManeuUsers.objects.filter(username=username).first()
