from django.db.models import Q

from maneu.models import ManeuOrder, ManeuReport


def report_delete(report_id='', admin_id=''):
    return ManeuReport.objects.filter(admin_id=admin_id, id=report_id).delete()


def order_index(admin_id='', star='', end=''):
    """
    全部订单
    """
    return ManeuOrder.objects.filter(admin_id=admin_id, time__gte=star, time__lte=end).order_by('-time').all()


def order_id(order_id='', admin_id=''):
    """
    查找指定订单
    根据时间排序
    """
    return ManeuOrder.objects.filter(id=order_id, admin_id=admin_id).first()


def order_delete(admin_id='', order_id=''):
    """
    查找指定订单a
    根据时间排序
    """
    return ManeuOrder.objects.filter(admin_id=admin_id, id=order_id).delete()


def order_search(text='', admin_id=''):
    return ManeuOrder.objects.filter(Q(name__icontains=text, admin_id=admin_id) | Q(phone__icontains=text, admin_id=admin_id)).all()


def order_insert(name='', time='', call='', content='', guest_id='', admin_id='', store_id='', report_id='', remark=''):
    return ManeuOrder.objects.create(name=name, time=time, phone=call, guest_id=guest_id, admin_id=admin_id,
                                     store_id=store_id, report_id=report_id, remark=remark, content=content)


def order_update(admin_id='', order_id='', name='', call='', time="", remark="", content=''):
    return ManeuOrder.objects.filter(id=order_id, admin_id=admin_id).update(name=name, phone=call, time=time, remark=remark, content=content)
