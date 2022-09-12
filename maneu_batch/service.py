from maneu_batch.models import Batch


def batch_list():
    return Batch.objects.order_by('-c_time').all()


def batch_list_ByName(arg):
    return Batch.objects.filter(c_name=arg).order_by('-c_time').all()


def batch_list_ByPhone(arg):
    return Batch.objects.filter(c_phone=arg).order_by('-c_time').all()


def batch_detail(order_id):
    return Batch.objects.filter(order_id=order_id).get()


def batch_insert(form, order, order_id):
    try:
        Batch.objects.create(
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
        Batch.objects.filter(order_id=order_id).first().delete()
        return True
    except BaseException as msg:
        print(msg)
        return False
