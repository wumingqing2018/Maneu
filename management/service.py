from django.shortcuts import HttpResponse

from management import my_lib
from management.models import ProductManage

# Create your service here.


def add_order(order):
    item = ProductManage.objects.create(
        order_id=my_lib.creste_order_id(),

        c_name=order['c_name'],
        c_phone=order['c_phone'],
        c_time=my_lib.current_time(),

        u_name='聪少',
        u_phone='13640651582',
        u_time=my_lib.current_time(),
        frame=order['frame'],

        l_glasses=order['l_glasses'],
        l_sphere=order['l_sphere'],
        l_astigmatic=order['l_astigmatic'],
        l_deviation=order['l_deviation'],
        l_add=order['l_add'],
        l_pd=order['l_pd'],

        r_glasses=order['r_glasses'],
        r_sphere=order['r_sphere'],
        r_astigmatic=order['r_astigmatic'],
        r_deviation=order['r_deviation'],
        r_add=order['r_add'],
        r_pd=order['r_pd'],

        token=my_lib.token(),
        todo=order['todo'],
    )
    return item


def find_all_order():
    item = ProductManage.objects.all()
    return item


def find_one_order_with_order_id(order_id):
    item = ProductManage.objects.filter(order_id=order_id).first()
    return item


def find_all_order_with_order_id(order_id):
    item = {}
    if type(order_id) == int:
        try:
            item['object'] = ProductManage.objects.filter(order_id=order_id)
            item['state'] = True
            item['error'] = None
        except BaseException as msg:
            item['object'] = None
            item['state'] = False
            item['error'] = msg
    else:
        item['object'] = None
        item['state'] = False
        item['error'] = "参数格式错误"
    return HttpResponse(item)


def delete_one_order_with_order_id(order_id):
    try:
        contact_list = ProductManage.objects.filter(order_id=order_id).first()
        contact_list.delete()
        return HttpResponse(True)
    except BaseException as msg:
        return HttpResponse(msg)


def find_one_order_with_data(u_time):
    try:
        return ProductManage.objects.filter(u_time__gt=u_time).order_by('-u_time')
    except:
        return []
