from maneu_order.models import ManeuClass


def class_list(user_id=''):
    return ManeuClass.objects.filter(user_id=user_id).all()


def class_insert(user_id='', name='', series='', color='', price=''):
    return ManeuClass.objects.create(user_id=user_id, name=name, series=series, color=color, price=price)


def class_delete(user_id='', id=''):
    return ManeuClass.objects.filter(user_id=user_id, id=id).delete()
