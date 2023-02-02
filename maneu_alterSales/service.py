from maneu_alterSales.models import ManeuAftersales


def ManeuAfterSales_orderID(order_id=''):
    return ManeuAftersales.objects.filter(order_id=order_id).order_by('-time').all()


def ManeuAfterSales_insert(order_id='', content=''):
    return ManeuAftersales.objects.create(order_id=order_id, content=content)


def ManeuAfterSales_delete_order_id(order_id=''):
        return ManeuAftersales.objects.filter(order_id=order_id).all().delete()


def ManeuAfterSales_delete_id(id=''):
    return ManeuAftersales.objects.filter(id=id).all().delete()


def ManeuAfterSales_index():
    return ManeuAftersales.objects.all().order_by('-time')