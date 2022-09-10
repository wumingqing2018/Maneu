from maneu_order.models import ManeuGuess
from maneu_order.models import ManeuOrderV2
from maneu_order.models import ManeuStore
from maneu_order.models import ManeuSubjectiveRefraction
from maneu_order.models import ManeuUsers
from maneu_order.models import ManeuVisionSolutions
from maneu_users.models import ManeuUsers


def find_user_username(username=''):
    """
    通过username查找用户
    """
    return ManeuUsers.objects.filter(username=username).first()


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
