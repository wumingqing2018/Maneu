from maneu.models import *


def find_store_id(id=''):
    try:
        return ManeuStore.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def Index_insert(admin_id, time='', guess_log='', service_log='', orderv1_log='', orderv2_log=''):
    return ManeuIndex.objects.create(time=time, admin_id=admin_id, guess_log=guess_log, service_log=service_log, orderv1_log=orderv1_log, orderv2_log=orderv2_log)


def find_index(admin_id='', year='', month=''):
    return ManeuIndex.objects.filter(admin_id=admin_id, time__year=year, time__month=month).all()


def find_guess_month(admin_id='', year=0, month=0,):
    return ManeuGuess.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def find_orderV1_month(admin_id='', year=0, month=0,):
    return ManeuOrderv1.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def find_orderV2_month(admin_id='', year=0, month=0,):
    return ManeuOrderv2.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def find_service_month(admin_id='', year=0, month=0,):
    return ManeuService.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def find_guess_day(admin_id='', year=0, month=0, day=0):
    return ManeuGuess.objects.filter(time__year=year, time__month=month, day=day, admin_id=admin_id).all()


def find_orderV1_day(admin_id='', year=0, month=0, day=0):
    return ManeuOrderv1.objects.filter(time__year=year, time__month=month, day=day, admin_id=admin_id).all()


def find_orderV2_day(admin_id='', year=0, month=0, day=0):
    return ManeuOrderv2.objects.filter(time__year=year, time__month=month, day=day, admin_id=admin_id).all()


def find_service_day(admin_id='', year=0, month=0, day=0):
    return ManeuService.objects.filter(time__year=year, time__month=month, day=day, admin_id=admin_id).all()
