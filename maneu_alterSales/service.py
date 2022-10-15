from .models import ManeuAftersales


def ManeuAfterSales_list(order_id=''):
    try:
        return ManeuAftersales.objects.filter(order_id=order_id).order_by('-time').all()
    except BaseException as msg:
        print(msg)
        return


def ManeuAfterSales_content(order_id=''):
    try:
        return ManeuAftersales.objects.filter(order_id=order_id).first()
    except BaseException as msg:
        print(msg)
        return None


def ManeuAfterSales_insert(order_id='', content=''):
    try:
        return ManeuAftersales.objects.create(order_id=order_id, content=content)
    except BaseException as msg:
        print(msg)
        return None


def ManeuAfterSales_delete_order_id(order_id=''):
    try:
        return ManeuAftersales.objects.filter(order_id=order_id).all().delete()
    except BaseException as msg:
        print(msg)
        return None


def ManeuAfterSales_delete_id(id=''):
    try:
        return ManeuAftersales.objects.filter(id=id).all().delete()
    except BaseException as msg:
        print(msg)
        return None


def ManeuAfterSales_index():
    return ManeuAftersales.objects.all().order_by('-time')