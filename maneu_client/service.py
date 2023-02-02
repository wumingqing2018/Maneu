import json

from django.db.models import Q

from maneu_client.models import ManeuGuess
from maneu_client.models import ManeuSubjectiveRefraction


def subjectiverefraction_id(id=''):
    return ManeuSubjectiveRefraction.objects.filter(id=id).first()


def subjectiverefraction_guessID(guessID=''):
    return ManeuSubjectiveRefraction.objects.filter(guessID=guessID).first()


def guess_time(time, user_id):
    return ManeuGuess.objects.filter(time=time, user_id=user_id).order_by('-time').all()


def guess_delete(id=''):
    return ManeuGuess.objects.filter(id=id).delete()


def guess_all(user_id=''):
    return ManeuGuess.objects.filter(user_id=user_id).order_by('-time').all()


def guess_id(id=''):
    return ManeuGuess.objects.filter(id=id).first()


def guess_phone(phone=''):
    return ManeuGuess.objects.filter(phone=phone).first()


def guess_insert(contents='', user_id='', time=''):
    contents = json.loads(contents)
    return ManeuGuess.objects.create(time=time, user_id=user_id, name=contents['guess_name'], phone=contents['guess_phone'], sex=contents['sex'], age=contents['age'], ot=contents['OT'], em=contents['EM'], dfh=contents['DFH'], remark=contents['remark'])


def subjectiverefraction_insert(guess_id='', content=''):
    return ManeuSubjectiveRefraction.objects.create(guessID=guess_id, content=content)


def guess_update_user_id(id='', user_id=''):
    return ManeuGuess.objects.filter(id=id).update(user_id=user_id)


def guess_update_subjective_id(id='', subjective_id=''):
    return ManeuGuess.objects.filter(id=id).update(subjective_id=subjective_id)


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
