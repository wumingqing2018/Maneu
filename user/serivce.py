from .models import User
from common import common


def find_user(user_id):
    """
    通过user_id查找用户
    """
    return User.objects.filter(user_id=user_id).first()


def find_all_user():
    """查找所有用户"""
    return User.objects.all().order_by('-create_time')


def add_user(post):
    """添加用户"""
    try:
        item = User.objects.create(
            user_id=common.create_id(),
            username=post['username'],
            password=post['password'],
            email=post['email'],
            phone=post['phone'],
            level=post['level'],
            state=post['state'],
            create_time=common.today(),
        )
        return item
    except BaseException as msg:
        print(msg)
        return None
