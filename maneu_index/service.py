from maneu.models import *


def find_store_id(id=''):
    try:
        return ManeuStore.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_guess_month(users_id='', year=0, month=0,):
    return ManeuGuess.objects.filter(time__year=year, time__month=month, users_id=users_id).all()


def find_orderV1_month(users_id='', year=0, month=0,):
    return ManeuOrderv1.objects.filter(time__year=year, time__month=month, users_id=users_id).all()


def find_orderV2_month(users_id='', year=0, month=0,):
    return ManeuOrderv2.objects.filter(time__year=year, time__month=month, users_id=users_id).all()


def find_service_month(users_id='', year=0, month=0,):
    return ManeuService.objects.filter(time__year=year, time__month=month, users_id=users_id).all()


def find_guess_day(users_id='', year=0, month=0, day=0):
    return ManeuGuess.objects.filter(time__year=year, time__month=month, day=day, users_id=users_id).all()


def find_orderV1_day(users_id='', year=0, month=0, day=0):
    return ManeuOrderv1.objects.filter(time__year=year, time__month=month, day=day, users_id=users_id).all()


def find_orderV2_day(users_id='', year=0, month=0, day=0):
    return ManeuOrderv2.objects.filter(time__year=year, time__month=month, day=day, users_id=users_id).all()


def find_service_day(users_id='', year=0, month=0, day=0):
    return ManeuService.objects.filter(time__year=year, time__month=month, day=day, users_id=users_id).all()
