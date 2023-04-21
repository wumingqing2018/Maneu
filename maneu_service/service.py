from maneu.models import ManeuService


def ManeuService_index1(admin_id=''):
    return ManeuService.objects.filter(admin_id=admin_id).all()


def ManeuService_index2(order_id=''):
    return ManeuService.objects.filter(orderid=order_id).all()


def ManeuService_index3(guess_id=''):
    return ManeuService.objects.filter(guess_id=guess_id).all()


def ManeuService_orderID(order_id=''):
    return ManeuService.objects.filter(order_id=order_id).order_by('-time').all()


def ManeuService_insert(order_id='', content=''):
    return ManeuService.objects.create(order_id=order_id, content=content)


def ManeuService_delete_order_id(order_id=''):
    return ManeuService.objects.filter(order_id=order_id).all().delete()


def ManeuService_delete_id(id=''):
    return ManeuService.objects.filter(id=id).all().delete()
