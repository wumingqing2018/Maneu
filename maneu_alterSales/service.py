from maneu.models import ManeuAftersales


def ManeuAfterSales_orderID(order_id=''):
    return ManeuAftersales.objects.filter(order_id=order_id).order_by('-time').all()


def ManeuAfterSales_insert(order_id='', content=''):
    return ManeuAftersales.objects.create(order_id=order_id, content=content)


def ManeuAfterSales_delete_order_id(order_id=''):
    return ManeuAftersales.objects.filter(order_id=order_id).all().delete()


def ManeuAfterSales_delete_id(id=''):
    return ManeuAftersales.objects.filter(id=id).all().delete()


def ManeuAfterSales_index(time=''):
    return ManeuAftersales.objects.filter(time=time).order_by('-time').all()