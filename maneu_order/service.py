import json

from django.db.models import Q

from maneu.models import *


def ManeuOrder_index(admin_id='', star='', end=''):
    """
    全部订单
    """
    return ManeuOrder.objects.filter(admin_id=admin_id, time__gte=star, time__lte=end).order_by('-time').all()


def ManeuOrder_id(id='', admin_id=''):
    """
    查找指定订单
    根据时间排序
    """
    return ManeuOrder.objects.filter(id=id, admin_id=admin_id).first()


def ManeuOrder_delete(admin_id='', id=''):
    """
    查找指定订单a
    根据时间排序
    """
    return ManeuOrder.objects.filter(admin_id=admin_id, id=id).delete()


def ManeuOrder_Search(text='', admin_id=''):
    return ManeuOrder.objects.filter(Q(name__icontains=text, admin_id=admin_id) | Q(phone__icontains=text, admin_id=admin_id)).all()


def ManeuOrder_insert(name='', time='', call='', guess_id='', admin_id='', store_id='', vision_id='', remark=''):
    return ManeuOrder.objects.create(name=name, time=time, phone=call, guess_id=guess_id, admin_id=admin_id,
                                     store_id=store_id, vision_id=vision_id, remark=remark)


def ManeuOrder_update(id='', name='', phone='', time="", remark=""):
    return ManeuOrder.objects.filter(id=id).update(name=name, phone=phone, time=time, remark=remark)


def ManeuStore_id(id=''):
    return ManeuStore.objects.filter(id=id).first()


def ManeuStore_delete(id=''):
    return ManeuStore.objects.filter(id=id).all().delete()


def ManeuStore_insert(admin_id='', guess_id='', time='', content=''):
    return ManeuStore.objects.create(admin_id=admin_id, guess_id=guess_id, time=time, content=content)


def ManeuStore_update(content='', id=''):
    return ManeuStore.objects.filter(id=id).update(content=content)


def ManeuVision_id(id=''):
    return ManeuVision.objects.filter(id=id).first()


def ManeuVision_delete(id=''):
    return ManeuVision.objects.filter(id=id).delete()


def ManeuVision_insert(admin_id='', guess_id='', time='', content=''):
    return ManeuVision.objects.create(admin_id=admin_id, guess_id=guess_id, time=time, content=content)


def ManeuVision_update(id='', content=''):
    return ManeuVision.objects.filter(id=id).update(content=content)


def ManeuGuess_id(id=''):
    return ManeuGuess.objects.filter(id=id).first()


def ManeuGuess_phone(phone=''):
    return ManeuGuess.objects.filter(phone=phone).first()


def ManeuGuess_search(admin_id='', name='', time='', call='', sex='', age='', ot='', em='', dfh=''):
    return ManeuGuess.objects.get_or_create(admin_id=admin_id, name=name, phone=call,
                                            defaults={'sex': sex, 'age': age, 'ot': ot, 'em': em, 'dfh': dfh,
                                                      'time': time})


def ManeuGuess_update(id='', content=''):
    contents = json.loads(content)
    return ManeuGuess.objects.filter(id=id).update(name=contents['name'], phone=contents['phone'],
                                                   age=contents['age'],
                                                   sex=contents['sex'], ot=contents['OT'], em=contents['EM'],
                                                   dfh=contents['DFH'])


def ManeuService_insert(guess_id='', admin_id='', order_id='', content='', time=''):
    return ManeuService.objects.create(guess_id=guess_id, admin_id=admin_id, order_id=order_id, content=content,
                                       time=time)


def ManeuService_delete(admin_id='', id=''):
    return ManeuService.objects.filter(admin_id=admin_id, id=id).all().delete()


def ManeuService_update(admin_id='', id='', content=''):
    return ManeuService.objects.filter(admin_id=admin_id, id=id).update(content=content)


def ManeuService_orderID(order_id=''):
    return ManeuService.objects.filter(order_id=order_id).order_by('-time').all()


def ManeuService_delete_order_id(order_id=''):
    return ManeuService.objects.filter(order_id=order_id).all().delete()


def ManeuRefraction_id(guess_id=''):
    return ManeuRefraction.objects.filter(guess_id=guess_id).order_by('-time').first()


def ManeuReport_id(admin_id, id):
    return ManeuVision.objects.filter(admin_id=admin_id, id=id).first()
