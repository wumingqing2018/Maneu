from .models import User
from common import common


def find_user(user_id):
    """
    通过user_id查找用户
    """
    return User.objects.filter(user_id=user_id).first()


def find_all_user():
    """查找所有用户"""
    return User.objects.all()


def add_user(post):
    """添加用户"""
    try:
        item = User.objects.create(
            user_id=common.order_id(),
            username=post['username'],
            password=post['password'],
            nickname=post['nickname'],
            phone=post['phone'],
            join_time=common.today(),
            last_time=common.token(),
        )
        return item
    except:
        return None
