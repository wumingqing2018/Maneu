from maneu_order.models import ManeuGuess
from maneu_order.models import ManeuOrderV2
from maneu_order.models import ManeuStore
from maneu_order.models import ManeuSubjectiveRefraction
from maneu_order.models import ManeuUsers
from maneu_order.models import ManeuVisionSolutions
from maneu_users.models import ManeuUsers
from maneu_order.models import ManeuDatalogs


def find_user_username(username=''):
    """
    通过username查找用户
    """
    return ManeuUsers.objects.filter(username=username).first()


def find_order_month(users_id='', month=''):
    """
    全部订单
    """
    try:
        return ManeuOrderV2.objects.filter(time__month=month, users_id=users_id).order_by('-time').all()
    except BaseException as msg:
        return msg


def find_order_phone(phone=''):
    try:
        return ManeuOrderV2.objects.filter(phone=phone).order_by('-time').all()
    except BaseException as msg:
        print(msg)
        return None


def find_users_id(id=''):
    try:
        return ManeuUsers.objects.filter(user_id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_guess_id(id=''):
    try:
        return ManeuGuess.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_store_id(id=''):
    try:
        return ManeuStore.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_ManeuVisionSolutions_id(id=''):
    try:
        return ManeuVisionSolutions.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_subjectiverefraction_id(id=''):
    try:
        return ManeuSubjectiveRefraction.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def ManeuDatalogs_getorcreate(user_id, time, order_log):
    try:
        return ManeuDatalogs.objects.get_or_create(time=time, user_id=user_id, defaults={'user_id': user_id, 'order_log': order_log})
    except BaseException as msg:
        print(msg)
        return None


def ManeuDatalogs_update(user_id, time, order_log):
    try:
        return ManeuDatalogs.objects.filter(time=time, user_id=user_id,).update(order_log=order_log)
    except BaseException as msg:
        print(msg)
        return None


def ManeuDatalogs_List(user_id):
    try:
        return ManeuDatalogs.objects.filter(user_id=user_id).first()
    except BaseException as msg:
        return msg


def ManeuOrder_count(user_id,time):
    return ManeuOrderV2.objects.filter(time__range=[time + ' 00:00', time + ' 23:59'], users_id=user_id).count()


def ManeuStore_id(store_id):
    return ManeuStore.objects.filter(id=store_id).first()