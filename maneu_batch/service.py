from maneu_batch.models import ManeuBatch


def batch_list():
    return ManeuBatch.objects.order_by('-c_time').all()


def batch_list_ByName(arg):
    return ManeuBatch.objects.filter(c_name=arg).order_by('-c_time').all()


def batch_list_ByPhone(arg):
    return ManeuBatch.objects.filter(c_phone=arg).order_by('-c_time').all()


def batch_detail(order_id):
    return ManeuBatch.objects.filter(order_id=order_id).get()


def batch_insert(form, order, order_id):
    try:
        ManeuBatch.objects.create(
            order_id=order_id,
            c_name=form['c_name'],
            c_phone=form['c_phone'],
            order=order,
            remark=form['remark'],
        )
        return True
    except BaseException as msg:
        print(msg)
        return False


def batch_delete(order_id):
    try:
        ManeuBatch.objects.filter(order_id=order_id).first().delete()
        return True
    except BaseException as msg:
        print(msg)
        return False


def find_batch_date(date=''):
    try:
        return ManeuBatch.objects.filter(c_time__gt=date).all()
    except BaseException as msg:
        print(msg)
        return None
