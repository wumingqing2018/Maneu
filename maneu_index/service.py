from maneu.models import *


def find_store_id(id=''):
    try:
        return ManeuStore.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_guess_month(admin_id='', year=0, month=0,):
    return ManeuGuess.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def find_orderV1_month(admin_id='', year=0, month=0,):
    return ManeuOrderV1.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def find_orderV2_month(admin_id='', year=0, month=0,):
    return ManeuOrderV2.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def find_service_month(admin_id='', year=0, month=0,):
    return ManeuService.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def find_guess_day(admin_id='', year=0, month=0, day=0):
    return ManeuGuess.objects.filter(time__year=year, time__month=month, time__day=day, admin_id=admin_id).all()


def find_orderV1_day(admin_id='', year=0, month=0, day=0):
    return ManeuOrderV1.objects.filter(time__year=year, time__month=month, time__day=day, admin_id=admin_id).all()


def find_orderV2_day(admin_id='', year=0, month=0, day=0):
    return ManeuOrderV2.objects.filter(time__year=year, time__month=month, time__day=day, admin_id=admin_id).all()


def find_service_day(admin_id='', year=0, month=0, day=0):
    return ManeuService.objects.filter(time__year=year, time__month=month, time__day=day, admin_id=admin_id).all()
