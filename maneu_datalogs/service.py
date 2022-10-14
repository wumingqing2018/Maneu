from common.models import ManeuOrderV2
from common.models import ManeuStore


def find_order_month(users_id='', month=''):
    """
    全部订单
    """
    try:
        return ManeuOrderV2.objects.filter(time__month=month, users_id=users_id).order_by('-time').all()
    except BaseException as msg:
        return msg


def find_store_id(id=''):
    try:
        return ManeuStore.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None
