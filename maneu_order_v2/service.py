import json

from django.db.models import Q

from maneu.models import *


def ManeuOrderV2_all(admin_id=''):
    """
    全部订单
    """
    return ManeuOrderV2.objects.filter(admin_id=admin_id).order_by('-time').all()


def ManeuOrderV2_id(order_id='', admin_id=''):
    """
    查找指定订单
    根据时间排序
    """
    return ManeuOrderV2.objects.filter(id=order_id, admin_id=admin_id).first()


def ManeuOrderV2_delete(admin_id='', id=''):
    """
    查找指定订单a
    根据时间排序
    """
    return ManeuOrderV2.objects.filter(admin_id=admin_id, id=id).delete()


def ManeuOrderV2_Search(text='', admin_id=''):
    return ManeuOrderV2.objects.filter(Q(name=text, admin_id=admin_id) | Q(phone=text, admin_id=admin_id)).all()


def ManeuOrderV2_insert(name='', time='', phone='', guess_id='', admin_id=''):
    return ManeuOrderV2.objects.create(name=name, time=time, phone=phone, guess_id=guess_id, admin_id=admin_id)


def ManeuOrderV2_update(order_id='', name='', phone=''):
    return ManeuOrderV2.objects.filter(id=order_id).update(name=name, phone=phone)


def ManeuOrderV2_time(admin_id='', time=''):
    return ManeuOrderV2.objects.filter(admin_id=admin_id, time__day=time).order_by('-time').all()


def store_id(id=''):
    return ManeuStore.objects.filter(id=id).first()


def store_OrderID(orderid=''):
    return ManeuStore.objects.filter(orderid=orderid).first()


def ManeuStore_delete(id=''):
    return ManeuStore.objects.filter(id=id).delete()


def ManeuAdmin_id(id=''):
    return ManeuAdmin.objects.filter(id=id).first()


def ManeuVisionSolutions_orderID(orderid=''):
    return ManeuVisionSolutions.objects.filter(orderid=orderid).first()


def ManeuVisionSolutions_delete(id=''):
    return ManeuVisionSolutions.objects.filter(id=id).delete()


def ManeuVisionSolutions_insert(time='', order_id='', content=''):
    return ManeuVisionSolutions.objects.create(time=time, orderid=order_id, content=content)


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


def ManeuStore_insert(time='', order_id='', content=''):
    return ManeuStore.objects.create(time=time, orderid=order_id, content=content)


def ManeuStore_update(content='', id=''):
    return ManeuStore.objects.filter(id=id).update(content=content)


def ManeuStore_update_orderID(orderID='', id=''):
    return ManeuStore.objects.filter(id=id).update(orderID=orderID)


def guess_phone(phone):
    return ManeuGuess.objects.filter(phone=phone).first()


def ManeuGuess_search(admin_id='', name='', phone=''):
    return ManeuGuess.objects.filter(admin_id=admin_id, name=name, phone=phone).first()


def ManeuGuess_id(id=''):
    return ManeuGuess.objects.filter(id=id).first()


def delete_guess_id(id=''):
    return ManeuGuess.objects.filter(id=id).delete()


def ManeuGuess_insert(admin_id='', name='', phone=''):
    return ManeuGuess.objects.create(admin_id=admin_id, name=name, phone=phone)


def ManeuGuess_update(id='', content=''):
    contents = json.loads(content)
    return ManeuGuess.objects.filter(id=id).update(name=contents['guess_name'], phone=contents['guess_phone'],
                                                   sex=contents['sex'], ot=contents['OT'], em=contents['EM'],
                                                   dfh=contents['DFH'], remark=contents['remark'])

def ManeuService_delete_order_id(order_id=''):
    return ManeuService.objects.filter(order_id=order_id).all().delete()
