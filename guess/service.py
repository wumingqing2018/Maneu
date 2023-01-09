from maneu.models import ManeuGuess
from maneu.models import ManeuOrderV2
from maneu.models import ManeuStore
from maneu.models import ManeuSubjectiveRefraction
from maneu.models import ManeuUsers
from maneu.models import ManeuVisionSolutions


def find_guess_id(id=''):
    try:
        return ManeuGuess.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_order_GuessId(guessId=''):
    return ManeuOrderV2.objects.filter(guess_id=guessId).order_by('-time').all()


def find_order_Id(orderID=''):
    return ManeuOrderV2.objects.filter(id=orderID).first()


def find_ManeuVisionSolutions_id(id=''):
    return ManeuVisionSolutions.objects.filter(id=id).first()


def find_store_id(id=''):
    return ManeuStore.objects.filter(id=id).first()


def find_users_id(id):
    return ManeuUsers.objects.filter(id=id).first()


def find_subject_id(id):
    return ManeuSubjectiveRefraction.objects.filter(id=id).first()
