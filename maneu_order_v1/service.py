from maneu.models import ManeuOrderV1


def batch_all(admin_id=''):
    return ManeuOrderV1.objects.filter(admin_id=admin_id).order_by('-time').all()


def batch_list_ByName(arg):
    return ManeuOrderV1.objects.filter(name=arg).order_by('-time').all()


def batch_list_ByPhone(arg):
    return ManeuOrderV1.objects.filter(phone=arg).order_by('-time').all()


def batch_detail(id=''):
    return ManeuOrderV1.objects.filter(id=id).first()


def batch_insert(form, admin_id='', contents=''):
    ManeuOrderV1.objects.create(name=form['name'], phone=form['phone'], admin_id=admin_id, contents=contents)


def batch_delete(id=''):
    return ManeuOrderV1.objects.filter(id=id).all().delete()


def find_batch_date(date=''):
    try:
        return ManeuOrderV1.objects.filter(time__gt=date).all()
    except BaseException as msg:
        print(msg)
        return None
