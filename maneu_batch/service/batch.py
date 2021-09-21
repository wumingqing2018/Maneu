from maneu_batch.models import Batch
from common.common import create_id
from common.common import current_time


def batch_list():
    return Batch.objects.order_by('-c_time')[0:20]


def batch_detail(order_id):
    return Batch.objects.filter(order_id=order_id).get()


def batch_insert(form, order):
    try:
        Batch.objects.create(
            order_id=create_id(),
            c_name=form['c_name'],
            c_phone=form['c_phone'],
            order=order,
            remark=form['remark'],
        )
        return True
    except BaseException as msg:
        print(msg)
        return False
