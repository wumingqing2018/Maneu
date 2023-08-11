from maneu.models import ManeuService


def ManeuService_index(admin_id=''):
    return ManeuService.objects.filter(admin_id=admin_id).all()


def ManeuService_orderID(order_id=''):
    return ManeuService.objects.filter(order_id=order_id).order_by('-time').all()


def ManeuService_insert(order_id='', guess_id='', admin_id='', content='', time=''):
    return ManeuService.objects.create(guess_id=guess_id, admin_id=admin_id, order_id=order_id, content=content,
                                       time=time)


def ManeuService_delete_order_id(order_id=''):
    return ManeuService.objects.filter(order_id=order_id).all().delete()


def ManeuService_delete_id(id=''):
    return ManeuService.objects.filter(id=id).all().delete()


def ManeuService_delete(admin_id='', id=''):
    return ManeuService.objects.filter(admin_id=admin_id, id=id).delete()
