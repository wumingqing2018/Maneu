from maneu.models import *


def ManeuOrder_index(admin_id='', start='', end=''):
    return ManeuOrder.objects.filter(time__gte=start, time__lte=end, admin_id=admin_id).all()


def ManeuGuess_index(admin_id='', start='', end=''):
    return ManeuGuess.objects.filter(time__gte=start, time__lte=end, admin_id=admin_id).all()
