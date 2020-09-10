from .models import User
from management import my_lib


# Create your service here.


def find_all_user():
    item = User.objects.all()
    return item


def add_user(post):
    item = User.objects.create(
        user_id=my_lib.creste_order_id(),
        username=post['username'],
        password=post['password'],
        nickname=post['nickname'],
        phone=post['phone'],
        join_time=my_lib.current_day(),
        last_time=my_lib.current_day(),
    )


def find_user(user_id):
    return User.objects.filter(user_id=user_id).first()
