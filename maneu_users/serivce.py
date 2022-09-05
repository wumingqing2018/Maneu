from common import common
from maneu_users.models import User


def find_user(user_id):
    """
    通过user_id查找用户
    """
    return User.objects.filter(user_id=user_id).first()


def find_user_username(username=''):
    """
    通过username查找用户
    """
    return User.objects.filter(username=username).first()


def find_username_password(username, password):
    return User.objects.filter(username=username, password=password).first()


def find_user_all():
    """查找所有用户"""
    return User.objects.filter(level='1').order_by('-create_time')


def add_user(post):
    """添加用户"""
    try:
        return User.objects.create(
            user_id=common.create_id(),
            username=post['username'],
            password=post['password'],
            email=post['email'],
            phone=post['phone'],
            level='1',
            state='1',
        )
    except BaseException as msg:
        return str(msg)


def user_delete(user_id):
    return User.objects.filter(user_id=user_id).delete()


def user_update(old_password='', user_id='', nickname='', password='', email='', phone='', remark=''):
    try:
        User.objects.filter(user_id=user_id, password=old_password).update(nickname=nickname, password=password,
                                                                           email=email, phone=phone, remark=remark)
    except BaseException as msg:
        return str(msg)
