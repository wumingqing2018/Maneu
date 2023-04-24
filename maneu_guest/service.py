import json

from django.db.models import Q

from maneu.models import *


def subjectiverefraction_id(id=''):
    return ManeuSubjectiveRefraction.objects.filter(id=id).first()


def subjectiverefraction_guessID(guess_id=''):
    return ManeuSubjectiveRefraction.objects.filter(guess_id=guess_id).first()


def guess_delete(id=''):
    return ManeuGuess.objects.filter(id=id).delete()


def guess_all(admin_id=''):
    return ManeuGuess.objects.filter(admin_id=admin_id).order_by('-time').all()


def guess_id(id=''):
    return ManeuGuess.objects.filter(id=id).first()


def guess_insert(contents='', admin_id='', time=''):
    contents = json.loads(contents)
    return ManeuGuess.objects.create(time=time, admin_id=admin_id, name=contents['guess_name'], phone=contents['guess_phone'], sex=contents['sex'], age=contents['age'], ot=contents['OT'], em=contents['EM'], dfh=contents['DFH'], remark=contents['remark'])


def subjectiverefraction_insert(guess_id='', content=''):
    return ManeuSubjectiveRefraction.objects.create(guess_id=guess_id, content=content)


def find_Guess_search(text='', admin_id=''):
    return ManeuGuess.objects.filter(Q(name=text, admin_id=admin_id) | Q(phone=text, admin_id=admin_id)).order_by('-time').all()


def find_Guess_time(admin_id='', time=''):
    return ManeuGuess.objects.filter(admin_id=admin_id, time__day=time).all()


def guess_update(id='', content=''):
    contents = json.loads(content)
    return ManeuGuess.objects.filter(id=id).update(name=contents['guess_name'],
                                                   phone=contents['guess_phone'], sex=contents['sex'], age=contents['age'],
                                                   ot=contents['OT'], em=contents['EM'], dfh=contents['DFH'],
                                                   remark=contents['remark'])


def subjective_update(id='', content=''):
    return ManeuSubjectiveRefraction.objects.filter(id=id).update(content=content)


def find_ManeuOrderV2_guess_id(guess_id=''):
    return ManeuOrderV2.objects.filter(guess_id=guess_id).order_by('-time').all()
