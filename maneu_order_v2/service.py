import json

from django.db.models import Q

from maneu.models import *


def ManeuOrderV2_all(admin_id=''):
    """
    全部订单
    """
    return ManeuOrderV2.objects.filter(admin_id=admin_id).order_by('-time').all()


def ManeuOrderV2_id(id='', admin_id=''):
    """
    查找指定订单
    根据时间排序
    """
    return ManeuOrderV2.objects.filter(id=id, admin_id=admin_id).first()


def ManeuOrderV2_time(admin_id='', time=''):
    return ManeuOrderV2.objects.filter(admin_id=admin_id, time__day=time).order_by('-time').all()


def ManeuOrderV2_delete(admin_id='', id=''):
    """
    查找指定订单a
    根据时间排序
    """
    return ManeuOrderV2.objects.filter(admin_id=admin_id, id=id).delete()


def ManeuOrderV2_Search(text='', admin_id=''):
    return ManeuOrderV2.objects.filter(Q(name__icontains=text, admin_id=admin_id) | Q(phone__icontains=text, admin_id=admin_id)).all()


def ManeuOrderV2_insert(name='', time='', phone='', guess_id='', admin_id='', store_id='', visionsolutions_id=''):
    return ManeuOrderV2.objects.create(name=name, time=time, phone=phone, guess_id=guess_id, admin_id=admin_id, store_id=store_id, visionsolutions_id=visionsolutions_id)


def ManeuOrderV2_update(order_id='', name='', phone=''):
    return ManeuOrderV2.objects.filter(id=order_id).update(name=name, phone=phone)




def ManeuStore_id(id=''):
    return ManeuStore.objects.filter(id=id).first()


def ManeuStore_delete(id=''):
    return ManeuStore.objects.filter(id=id).delete()


def ManeuStore_insert(time='', content=''):
    return ManeuStore.objects.create(time=time, content=content)


def ManeuStore_update(content='', id=''):
    return ManeuStore.objects.filter(id=id).update(content=content)




def ManeuVisionSolutions_id(id=''):
    return ManeuVisionSolutions.objects.filter(id=id).first()


def ManeuVisionSolutions_delete(id=''):
    return ManeuVisionSolutions.objects.filter(id=id).delete()


def ManeuVisionSolutions_insert(time='', content=''):
    return ManeuVisionSolutions.objects.create(time=time, content=content)


def ManeuVisionSolutions_update(id='', content=''):
    return ManeuVisionSolutions.objects.filter(id=id).update(content=content)





def ManeuGuess_id(id=''):
    return ManeuGuess.objects.filter(id=id).first()


def ManeuGuess_search(admin_id='', name='', phone=''):
    return ManeuGuess.objects.filter(admin_id=admin_id, name=name, phone=phone).first()


def ManeuGuess_insert(admin_id='', name='', phone=''):
    return ManeuGuess.objects.create(admin_id=admin_id, name=name, phone=phone)


def ManeuGuess_insert_v2(id='', admin_id='', name='', phone=''):
    return ManeuGuess.objects.create(id=id, admin_id=admin_id, name=name, phone=phone)


def ManeuGuess_update(id='', content=''):
    contents = json.loads(content)
    return ManeuGuess.objects.filter(id=id).update(name=contents['guess_name'], phone=contents['guess_phone'],
                                                   sex=contents['sex'], ot=contents['OT'], em=contents['EM'],
                                                   dfh=contents['DFH'], remark=contents['remark'])

def ManeuService_delete_order_id(order_id=''):
    return ManeuService.objects.filter(order_id=order_id).all().delete()
