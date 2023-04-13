from maneu.models import ManeuOrderv1


def batch_userid(userid='', time=''):
    return ManeuOrderv1.objects.filter(userid=userid, time=time).order_by('-time').all()


def batch_list():
    return ManeuOrderv1.objects.order_by('-time').all()


def batch_list_ByName(arg):
    return ManeuOrderv1.objects.filter(name=arg).order_by('-time').all()


def batch_list_ByPhone(arg):
    return ManeuOrderv1.objects.filter(phone=arg).order_by('-time').all()


def batch_detail(id=''):
    return ManeuOrderv1.objects.filter(id=id).first()


def batch_insert(form, order, order_id):
    try:
        ManeuOrderv1.objects.create(
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
    return ManeuOrderv1.objects.filter(id=id).all().delete()


def find_batch_date(date=''):
    try:
        return ManeuOrderv1.objects.filter(time__gt=date).all()
    except BaseException as msg:
        print(msg)
        return None
