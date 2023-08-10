from django.db.models import Q

from maneu.models import *


def ManeuGuess_id(admin_id='', id=''):
    return ManeuGuess.objects.filter(admin_id=admin_id, id=id).first()


def ManeuGuess_all(admin_id=''):
    return ManeuGuess.objects.filter(admin_id=admin_id).order_by('-time').all()


def ManeuGuess_time(admin_id='', time=''):
    return ManeuGuess.objects.filter(admin_id=admin_id, time=time).all()


def ManeuGuess_insert(admin_id='', time='', name='', phone='', sex='', age='', ot='', em='', dfh='', remark=''):
    return ManeuGuess.objects.create(time=time, admin_id=admin_id, name=name, phone=phone, sex=sex, age=age, ot=ot, em=em, dfh=dfh, remark=remark)


def ManeuGuess_update(id='', time='', name='', phone='', sex='', age='', ot='', em='', dfh='', remark=''):
    return ManeuGuess.objects.filter(id=id).update(time=time, name=name, phone=phone, sex=sex, age=age, ot=ot, em=em, dfh=dfh, remark=remark)


def ManeuGuess_search(text='', admin_id=''):
    return ManeuGuess.objects.filter(Q(name__contains=text, admin_id=admin_id) | Q(phone__contains=text, admin_id=admin_id)).order_by('-time').all()


def ManeuGuess_delete(id=''):
    return ManeuGuess.objects.filter(id=id).delete()


def ManeuSubjectiveRefraction_id(id=''):
    return ManeuRefraction.objects.filter(id=id).first()


def ManeuSubjectiveRefraction_all(guess_id=''):
    return ManeuRefraction.objects.filter(guess_id=guess_id).order_by('-time').all()


def ManeuSubjectiveRefraction_insert(admin_id='', guess_id='', time='', content=''):
    return ManeuRefraction.objects.create(time=time, admin_id=admin_id, guess_id=guess_id, content=content)


def ManeuSubjectiveRefraction_update(id='', admin_id='', content=''):
    return ManeuRefraction.objects.filter(id=id, admin_id=admin_id).update(content=content)


def ManeuSubjectiveRefraction_delete(id='', admin_id=''):
    return ManeuRefraction.objects.filter(id=id, admin_id=admin_id).delete()


def ManeuVisionSolutions_all(guess_id=''):
    return ManeuVision.objects.filter(guess_id=guess_id).order_by('-time').all()


def ManeuOrderV2_all(guess_id=''):
    return ManeuOrderV2.objects.filter(guess_id=guess_id).order_by('-time').all()


def ManeuService_all(guess_id=''):
    return ManeuService.objects.filter(guess_id=guess_id).order_by('-time').all()