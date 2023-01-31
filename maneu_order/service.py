import json

from django.db.models import Q

from maneu_order.models import ManeuAftersales
from maneu_order.models import ManeuGuess
from maneu_order.models import ManeuOrderV2
from maneu_order.models import ManeuStore
from maneu_order.models import ManeuSubjectiveRefraction
from maneu_order.models import ManeuUsers
from maneu_order.models import ManeuVisionSolutions


def ManeuOrderV2_all(users_id=''):
    """
    全部订单
    """
    return ManeuOrderV2.objects.filter(users_id=users_id).order_by('-time').all()


def ManeuOrderV2_today(users_id='', time=''):
    """
    全部订单
    """
    return ManeuOrderV2.objects.filter(users_id=users_id, time=time).order_by('-time').all()



def ManeuOrderV2_id(order_id='', users_id=''):
    """
    查找指定订单
    根据时间排序
    """
    return ManeuOrderV2.objects.filter(id=order_id, users_id=users_id).first()


def ManeuOrderV2_delete(users_id='', id=''):
    """
    查找指定订单a
    根据时间排序
    """
    return ManeuOrderV2.objects.filter(users_id=users_id, id=id).delete()


def find_order_phone(phone=''):
    return ManeuOrderV2.objects.filter(phone=phone).order_by('-time').all()


def guess_id(id=''):
    return ManeuGuess.objects.filter(id=id).first()


def ManeuGuess_id(id=''):
    return ManeuGuess.objects.filter(id=id).first()


def delete_guess_id(id=''):
    return ManeuGuess.objects.filter(id=id).delete()


def store_id(id=''):
    return ManeuStore.objects.filter(id=id).first()


def store_OrderID(OrderID=''):
    return ManeuStore.objects.filter(orderID=OrderID).first()


def ManeuStore_delete(id=''):
    return ManeuStore.objects.filter(id=id).delete()


def users_id(id):
    return ManeuUsers.objects.filter(id=id).first()


def ManeuUsers_id(id=''):
    return ManeuUsers.objects.filter(id=id).first()


def ManeuOrderV2_Search(text='', users_id=''):
    return ManeuOrderV2.objects.filter(Q(name=text) | Q(phone=text, users_id=users_id)).order_by('-time').all()


def ManeuVisionSolutions_orderID(order_id=''):
    return ManeuVisionSolutions.objects.filter(orderID=order_id).first()


def ManeuVisionSolutions_delete(id=''):
    return ManeuVisionSolutions.objects.filter(id=id).delete()


def ManeuVisionSolutions_insert(order_id='', content=''):
    return ManeuVisionSolutions.objects.create(orderID=order_id, content=content)


def ManeuVisionSolutions_update(id='', content=''):
    return ManeuVisionSolutions.objects.filter(id=id).update(content=content)


def ManeuVisionSolutions_update_orderID(id='', orderID=''):
    return ManeuVisionSolutions.objects.filter(id=id).update(orderID=orderID)


def subjectiverefraction_orderID(order_id=''):
    return ManeuSubjectiveRefraction.objects.filter(orderID=order_id).first()


def ManeuSubjectiveRefraction_delete(id=''):
    return ManeuSubjectiveRefraction.objects.filter(id=id).first()


def ManeuSubjectiveRefraction_insert(content=''):
    return ManeuSubjectiveRefraction.objects.create(content=content)


def ManeuSubjectiveRefraction_update(id='', content=''):
    return ManeuSubjectiveRefraction.objects.filter(id=id).update(content=content)


def ManeuGuess_insert(content='', user_id=''):
    contents = json.loads(content)
    return ManeuGuess.objects.create(user_id=user_id, name=contents['guess_name'], phone=contents['guess_phone'],
                                     sex=contents['sex'], age=contents['age'], ot=contents['OT'], em=contents['EM'],
                                     dfh=contents['DFH'], remark=contents['remark'])


def ManeuGuess_update(id='', content=''):
    contents = json.loads(content)
    return ManeuGuess.objects.filter(id=id).update(name=contents['guess_name'], phone=contents['guess_phone'],
                                                   sex=contents['sex'], ot=contents['OT'], em=contents['EM'],
                                                   dfh=contents['DFH'], remark=contents['remark'])


def ManeuStore_insert(order_id='', content=''):
    return ManeuStore.objects.create(orderID=order_id, content=content)


def ManeuStore_update(content='', id=''):
    return ManeuStore.objects.filter(id=id).update(content=content)


def ManeuStore_update_orderID(orderID='', id=''):
    return ManeuStore.objects.filter(id=id).update(orderID=orderID)


def ManeuOrderV2_insert(name='', time='', phone='', guess_id='', users_id=''):
    if time:
        return ManeuOrderV2.objects.create(name=name, time=time, phone=phone, guess_id=guess_id, users_id=users_id)
    else:
        return ManeuOrderV2.objects.create(name=name, phone=phone, guess_id=guess_id, users_id=users_id)


def ManeuOrderV2_update(order_id='', name='', phone=''):
    return ManeuOrderV2.objects.filter(id=order_id).update(name=name, phone=phone)


def ManeuAfterSales_delete(order_id=''):
    return ManeuAftersales.objects.filter(order_id=order_id).delete()


def guess_phone(phone):
    return ManeuGuess.objects.filter(phone=phone).first()
