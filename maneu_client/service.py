import json

from django.db.models import Q

from maneu_client.models import ManeuGuess
from maneu_client.models import ManeuOrderV2
from maneu_client.models import ManeuSubjectiveRefraction
from maneu_order.models import ManeuUsers


def subjectiverefraction_id(id=''):
    return ManeuSubjectiveRefraction.objects.filter(id=id).first()


def guess_time(time, user_id):
    return ManeuGuess.objects.filter(time=time, user_id=user_id).order_by('-time').all()


def users_id(id=''):
    return ManeuUsers.objects.filter(id=id).first()


def guess_delete(id=''):
    return ManeuGuess.objects.filter(id=id).delete()


def guess_all(user_id=''):
    return ManeuGuess.objects.filter(user_id=user_id).order_by('-time').all()


def guess_id(id=''):
    return ManeuGuess.objects.filter(id=id).first()


def guess_phone(phone=''):
    return ManeuGuess.objects.filter(phone=phone).first()


def guess_insert(contents='', subjective_id='', user_id=''):
    return ManeuGuess.objects.create(user_id=user_id, subjective_id=subjective_id, name=contents['guess_name'], phone=contents['guess_phone'], sex=contents['sex'], age=contents['age'], ot=contents['OT'], em=contents['EM'], dfh=contents['DFH'], remark=contents['remark'])


def subjectiverefraction_insert(content=''):
    return ManeuSubjectiveRefraction.objects.create(content=content)


def guess_update_user_id(id='', user_id=''):
    return ManeuGuess.objects.filter(id=id).update(user_id=user_id)


def guess_update_subjective_id(id='', subjective_id=''):
    return ManeuGuess.objects.filter(id=id).update(subjective_id=subjective_id)


def order_all(users_id=''):
    """
    全部订单
    """
    return ManeuOrderV2.objects.filter(users_id=users_id).order_by('-time').all()


def guess_search(text='', users_id=''):
    return ManeuGuess.objects.filter(Q(name=text) | Q(phone=text, user_id=users_id)).order_by('-time').all()


def guess_update(id='', content=''):
    contents = json.loads(content)
    return ManeuGuess.objects.filter(id=id).update(name=contents['guess_name'],
                                                   phone=contents['guess_phone'], sex=contents['sex'], age=contents['age'],
                                                   ot=contents['OT'], em=contents['EM'], dfh=contents['DFH'],
                                                   remark=contents['remark'])


def subjective_update(id='', content=''):
    return ManeuSubjectiveRefraction.objects.filter(id=id).update(content=content)


def order_phone(phone=''):
    return ManeuOrderV2.objects.filter(phone=phone).all()
