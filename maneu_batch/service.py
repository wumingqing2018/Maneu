from maneu_batch.models import ManeuBatch


def batch_list():
    return ManeuBatch.objects.order_by('-time').all()


def batch_list_ByName(arg):
    return ManeuBatch.objects.filter(name=arg).order_by('-time').all()


def batch_list_ByPhone(arg):
    return ManeuBatch.objects.filter(phone=arg).order_by('-time').all()


def batch_detail(order_id):
    return ManeuBatch.objects.filter(order_id=order_id).get()


def batch_insert(form, order, order_id):
    try:
        ManeuBatch.objects.create(
            order_id=order_id,
            name=form['name'],
            phone=form['phone'],
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
        return ManeuBatch.objects.filter(time__gt=date).all()
    except BaseException as msg:
        print(msg)
        return None
