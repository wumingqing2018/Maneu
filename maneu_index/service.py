from maneu.models import *


def ManeuGuess_month(admin_id='', year=0, month=0, ):
    return ManeuGuess.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def ManeuOrder_month(admin_id='', year=0, month=0, ):
    return ManeuOrder.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def ManeuService_month(admin_id='', year=0, month=0, ):
    return ManeuService.objects.filter(time__year=year, time__month=month, admin_id=admin_id).all()


def ManeuGuess_day(admin_id='', year=0, month=0, day=0):
    return ManeuGuess.objects.filter(time__year=year, time__month=month, time__day=day, admin_id=admin_id).all()


def ManeuOrder_day(admin_id='', year=0, month=0, day=0):
    return ManeuOrder.objects.filter(time__year=year, time__month=month, time__day=day, admin_id=admin_id).all()


def ManeuService_day(admin_id='', year=0, month=0, day=0):
    return ManeuService.objects.filter(time__year=year, time__month=month, time__day=day, admin_id=admin_id).all()
