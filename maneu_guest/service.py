from django.db.models import Q

from maneu.models import *


def ManeuGuest_index(admin_id='', start='', end=''):
    return ManeuGuess.objects.filter(admin_id=admin_id, time__gte=start, time__lte=end).order_by('-time').all()


def ManeuGuest_Search(admin_id='', text=''):
    return ManeuGuess.objects.filter(Q(name__icontains=text, admin_id=admin_id) | Q(phone__icontains=text, admin_id=admin_id)).order_by('-time').all()


def ManeuGuest_id(admin_id='', id=''):
    return ManeuGuess.objects.filter(admin_id=admin_id, id=id).first()


def ManeuGuess_insert(admin_id='', time='', name='', phone='', sex='', age='', ot='', em='', dfh='', remark=''):
    return ManeuGuess.objects.get_or_create(admin_id=admin_id, name=name, phone=phone,
                                            defaults={'sex': sex, 'age': age, 'ot': ot, 'em': em, 'dfh': dfh,
                                                      'time': time, 'remark': remark})


def ManeuGuess_update(admin_id='', id='', time='', name='', phone='', sex='', age='', ot='', em='', dfh='', remark=''):
    return ManeuGuess.objects.filter(id=id, admin_id=admin_id).update(time=time, name=name, phone=phone, sex=sex, age=age, ot=ot, em=em, dfh=dfh, remark=remark)


def ManeuGuess_delete(id='', admin_id=''):
    return ManeuGuess.objects.filter(id=id, admin_id=admin_id).delete()


def ManeuSubjectiveRefraction_id(id=''):
    return ManeuRefraction.objects.filter(id=id).first()


def ManeuRefraction_all(guest_id=''):
    return ManeuRefraction.objects.filter(guest_id=guest_id).order_by('-time').all()


def ManeuSubjectiveRefraction_insert(admin_id='', guest_id='', time='', content=''):
    return ManeuRefraction.objects.create(time=time, admin_id=admin_id, guest_id=guest_id, content=content)


def ManeuSubjectiveRefraction_update(id='', admin_id='', content=''):
    return ManeuRefraction.objects.filter(id=id, admin_id=admin_id).update(content=content)


def ManeuSubjectiveRefraction_delete(id='', admin_id=''):
    return ManeuRefraction.objects.filter(id=id, admin_id=admin_id).delete()


def ManeuOrderV2_all(guest_id=''):
    return ManeuOrderV2.objects.filter(guest_id=guest_id).order_by('-time').all()


def ManeuService_all(guest_id=''):
    return ManeuService.objects.filter(guest_id=guest_id).order_by('-time').all()
