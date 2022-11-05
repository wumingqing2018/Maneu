from maneu_client.models import ManeuOrderV2
from maneu_client.models import ManeuSubjectiveRefraction
from maneu_client.models import ManeuGuess
from maneu_order.models import ManeuUsers
import json
from django.db.models import Q


def find_subjectiverefraction_id(id=''):
    return ManeuSubjectiveRefraction.objects.filter(id=id).first()


def find_users_id(id=''):
    return ManeuUsers.objects.filter(id=id).first()


def find_users_search(id=''):
    return ManeuUsers.objects.filter(id=id).first()



def find_guess_list(user_id=''):
    return ManeuGuess.objects.filter(user_id=user_id).order_by('-time').all()


def find_guess_id(id=''):
    return ManeuGuess.objects.filter(id=id).first()


def ManeuGuess_insert(content='', subjective_id='', user_id=''):
    try:
        contents = json.loads(content)
        return ManeuGuess.objects.create(user_id=user_id, subjective_id=subjective_id, name=contents['guess_name'], phone=contents['guess_phone'], sex=contents['sex'], age=contents['age'], ot=contents['OT'], em=contents['EM'], dfh=contents['DFH'], remark=contents['remark'])
    except BaseException as msg:
        return msg


def ManeuSubjectiveRefraction_insert(content=''):
    try:
        return ManeuSubjectiveRefraction.objects.create(content=content)
    except BaseException as msg:
        print(msg)
        return None


def guess_update_userIdandId(id='', user_id=''):
    return ManeuGuess.objects.filter(id=id).update(user_id=user_id)

def guess_update_subjective_id(id='', subjective_id=''):
    return ManeuGuess.objects.filter(id=id).update(subjective_id=subjective_id)


def find_order_all(users_id=''):
    """
    全部订单
    """
    return ManeuOrderV2.objects.filter(users_id=users_id).order_by('-time').all()

def find_ManeuGuess_search(date='', text='', users_id=''):
    if date and text:
        return ManeuGuess.objects.filter(Q(name=text) | Q(phone=text), Q(time__gt=date), Q(user_id=users_id)).order_by('-time').all()
    if date != '' and text == '':
        return ManeuGuess.objects.filter(Q(time__gt=date), Q(users_id=users_id)).order_by('-time').all()
    if date == '' and text != '':
        return ManeuGuess.objects.filter(Q(name=text) | Q(phone=text, user_id=users_id)).order_by('-time').all()
    return None
