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
        u_name=order['u_name'],
        u_phone=order['u_phone'],
        u_time=my_lib.current_time(),
        frame=order['frame'],
        todo=order['todo']
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
    return ProductManage.objects.filter(u_time=u_time)
