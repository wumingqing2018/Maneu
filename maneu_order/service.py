import json

from django.db.models import Q

from maneu_order.models import ManeuAfterSales
from maneu_order.models import ManeuGuess
from maneu_order.models import ManeuOrderV2
from maneu_order.models import ManeuStore
from maneu_order.models import ManeuSubjectiveRefraction
from maneu_order.models import ManeuUsers
from maneu_order.models import ManeuVisionSolutions
from maneu_order.models import ManeuDatalogs


def find_order_all(users_id=''):
    """
    全部订单
    """
    try:
        return ManeuOrderV2.objects.filter(users_id=users_id).order_by('-time').all()
    except BaseException as msg:
        print(msg)
        return None


def find_order_id(order_id='', users_id=''):
    """
    查找指定订单
    根据时间排序
    """
    try:
        return ManeuOrderV2.objects.filter(id=order_id, users_id=users_id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_order_time(time='', users_id=''):
    """
    查找指定订单
    根据时间排序
    """
    try:
        return ManeuOrderV2.objects.filter(time__range=time, users_id=users_id).all()
    except BaseException as msg:
        print(msg)
        return None


def delete_order_id(users_id='', id=''):
    """
    查找指定订单
    根据时间排序
    """
    try:
        order = ManeuOrderV2.objects.filter(users_id=users_id, id=id).all()
        return order.delete()
    except BaseException as msg:
        print(msg)
        return None


def find_order_phone(phone=''):
    try:
        return ManeuOrderV2.objects.filter(phone=phone).order_by('-time').all()
    except BaseException as msg:
        print(msg)
        return None


def find_guess_id(id=''):
    try:
        return ManeuGuess.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def delete_guess_id(id=''):
    try:
        guess = ManeuGuess.objects.filter(id=id).all()
        return guess.delete()
    except BaseException as msg:
        print(msg)
        return None


def find_store_id(id=''):
    try:
        return ManeuStore.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def delete_store_id(id=''):
    try:
        store = ManeuStore.objects.filter(id=id).first()
        return store.delete()
    except BaseException as msg:
        print(msg)
        return None


def find_users_all():
    try:
        return ManeuUsers.objects.filter().all()
    except BaseException as msg:
        print(msg)
        return None


def find_users_id(id):
    try:
        return ManeuUsers.objects.filter(user_id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_ManeuOrderV2_search(date='', text='', users_id=''):
    if date and text:
        return ManeuOrderV2.objects.filter(Q(name=text) | Q(phone=text), Q(time__gt=date), Q(users_id=users_id)).order_by('-time').all()
    if date != '' and text == '':
        return ManeuOrderV2.objects.filter(Q(time__gt=date), Q(users_id=users_id)).order_by('-time').all()
    if date == '' and text != '':
        return ManeuOrderV2.objects.filter(Q(name=text) | Q(phone=text, users_id=users_id)).order_by('-time').all()
    return None


def find_ManeuOrderV2_search_v1(date='', text='', users_id=''):
    return ManeuOrderV2.objects.filter(Q(name=text) | Q(phone=text), Q(time__gt=date), Q(users_id=users_id)).order_by(
        '-time').all()


def find_ManeuOrderV2_search_v2(date='', users_id=''):
    return ManeuOrderV2.objects.filter(Q(time__gt=date), Q(users_id=users_id)).order_by('-time').all()


def find_ManeuOrderV2_search_v3(text='', users_id=''):
    return ManeuOrderV2.objects.filter(users_id=users_id).filter(Q(name=text) | Q(phone=text)).order_by('-time').all()


def find_ManeuVisionSolutions_id(id=''):
    try:
        return ManeuVisionSolutions.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def delete_ManeuVisionSolutions_id(id=''):
    try:
        VisionSolutions = ManeuVisionSolutions.objects.filter(id=id).first()
        return VisionSolutions.delete()
    except BaseException as msg:
        print(msg)
        return None


def find_subjectiverefraction_id(id=''):
    try:
        return ManeuSubjectiveRefraction.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def delete_subjectiverefraction_id(id=''):
    try:
        subjectiverefraction = ManeuSubjectiveRefraction.objects.filter(id=id).first()
        return subjectiverefraction.delete()
    except BaseException as msg:
        print(msg)
        return None


def ManeuVisionSolutions_insert(content=''):
    try:
        return ManeuVisionSolutions.objects.create(content=content)
    except BaseException as msg:
        print(msg)
        return None


def ManeuVisionSolutions_update(id='', content=''):
    try:
        return ManeuVisionSolutions.objects.filter(id=id).update(content=content)
    except BaseException as msg:
        print(msg)
        return None


def ManeuSubjectiveRefraction_insert(content=''):
    try:
        return ManeuSubjectiveRefraction.objects.create(content=content)
    except BaseException as msg:
        print(msg)
        return None


def ManeuSubjectiveRefraction_update(id='', content=''):
    try:
        return ManeuSubjectiveRefraction.objects.filter(id=id).update(content=content)
    except BaseException as msg:
        print(msg)
        return None


def ManeuGuess_insert(content=''):
    try:
        contents = json.loads(content)
        return ManeuGuess.objects.create(name=contents['guess_name'], phone=contents['guess_phone'], sex=contents['sex'], age=contents['age'], ot=contents['OT'], em=contents['EM'], dfh=contents['DFH'], remark=contents['remark'])
    except BaseException as msg:
        return msg


def ManeuGuess_update(id='', content=''):
    try:
        contents = json.loads(content)
        return ManeuGuess.objects.filter(id=id).update(name=contents['guess_name'], phone=contents['guess_phone'], sex=contents['sex'], ot=contents['OT'], em=contents['EM'], dfh=contents['DFH'], remark=contents['remark'])
    except BaseException as msg:
        print(msg)
        return None


def ManeuStore_insert(content=''):
    try:
        return ManeuStore.objects.create(content=content)
    except BaseException as msg:
        print(msg)
        return None


def ManeuStore_update(content='', id=''):
    try:
        return ManeuStore.objects.filter(id=id).update(content=content)
    except BaseException as msg:
        print(msg)
        return None


def ManeuOrderV2_insert(name='', time='', phone='', guess_id='', users_id='', store_id='', visionsolutions_id='', subjectiverefraction_id=''):
    try:
        return ManeuOrderV2.objects.create(name=name, time=time, phone=phone, guess_id=guess_id, users_id=users_id,
                                           store_id=store_id, visionsolutions_id=visionsolutions_id,
                                           subjectiverefraction_id=subjectiverefraction_id)
    except BaseException as msg:
        print(msg)
        return msg


def ManeuOrderV2_update(order_id='', name='', phone=''):
    try:
        return ManeuOrderV2.objects.filter(id=order_id).update(name=name, phone=phone)
    except BaseException as msg:
        print(msg)
        return None


def ManeuAfterSales_list(order_id=''):
    try:
        return ManeuAfterSales.objects.filter(order_id=order_id).order_by('-time').all()
    except BaseException as msg:
        print(msg)
        return


def ManeuAfterSales_content(order_id=''):
    try:
        return ManeuAfterSales.objects.filter(order_id=order_id).first()
    except BaseException as msg:
        print(msg)
        return None


def ManeuAfterSales_insert(order_id='', content=''):
    try:
        return ManeuAfterSales.objects.create(order_id=order_id, content=content)
    except BaseException as msg:
        print(msg)
        return None


def ManeuAfterSales_delete(order_id=''):
    try:
        return ManeuAfterSales.objects.filter(order_id=order_id).all().delete()
    except BaseException as msg:
        print(msg)
        return None


def ManeuAfterSales_delete_id(id=''):
    try:
        return ManeuAfterSales.objects.filter(id=id).all().delete()
    except BaseException as msg:
        print(msg)
        return None


def Datalogs_id(users_id, time):
    return ManeuDatalogs.objects.filter(user_id=users_id, time__month=time).first()


def Datalogs_update(users_id, time, order_log):
    return ManeuDatalogs.objects.filter(user_id=users_id, time__month=time).update(order_log=order_log)


def Datalogs_time(users_id, time):
    return ManeuDatalogs.objects.filter(user_id=users_id, time__month=time).first()


def Datalogs_create(users_id, time,date,order_logs):
    return ManeuDatalogs.objects.create(user_id=users_id, time=date, order_log=order_logs)


def Datalogs_update(users_id, time,date,order_logs):
    return ManeuDatalogs.objects.filter(user_id=users_id, time__month=time).update(time=date, order_log=order_logs)


def ManeuStore_id(store_id):
    return ManeuStore.objects.filter(id=store_id).first()