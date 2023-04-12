from maneu.models import ManeuBatch


def batch_userid(userid='', time=''):
    return ManeuBatch.objects.filter(userid=userid, time=time).order_by('-time').all()


def batch_list():
    return ManeuBatch.objects.order_by('-time').all()


def batch_list_ByName(arg):
    return ManeuBatch.objects.filter(name=arg).order_by('-time').all()


def batch_list_ByPhone(arg):
    return ManeuBatch.objects.filter(phone=arg).order_by('-time').all()


def batch_detail(id=''):
    return ManeuBatch.objects.filter(id=id).first()


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


def batch_delete(id=''):
    return ManeuBatch.objects.filter(id=id).all().delete()


def find_batch_date(date=''):
    try:
        return ManeuBatch.objects.filter(time__gt=date).all()
    except BaseException as msg:
        print(msg)
        return None
