from common import verify
from django.forms import model_to_dict
from django.shortcuts import render

from maneu_order import service
from maneu_order.forms.orderUpdateForm import OrderUpdateForm
from maneu_order.forms.orderSearchForm import OrderSearchForm
from common.common import yesterday


def order_list(request):
    """查看今日订单"""
    orders = service.find_order_today()  # 查找今日订单
    print(yesterday(days=1))
    return render(request, 'order/order_list.html', {'orders': orders})


def order_detail(request):
    """
    查看订单详情
    校验请求模式 GET 校验order_id是否符合
    true
        渲染order_detail页面并传输参数order_id
    false
        渲染error页面并传输错误参数
    """ 
    order_id = verify.order_id_method_get(request)
    order = service.find_order_id(order_id)
    if order_id:
        return render(request, 'order/order_detail.html', {'maneu_order': order})
    else:
        return render(request, 'maneu/error.html', {'msg': '参数错误'})


def order_search(request):
    """查找指定订单"""
    phone = verify.phone_method_get(request)
    if phone:
        orders = service.find_order_phone(phone)  # 查找今日订单
        if orders:
            return render(request, 'order/order_list.html', {'orders': orders})
    return render(request, 'order/order_search.html', {'form': OrderSearchForm()})


def order_insert(request):
    """添加订单"""
    return render(request, 'order/order_insert.html')


def order_update(request):
    """更新订单"""
    order_id = verify.order_id_method_get(request)
    if order_id:
        orders = service.find_order_id(order_id)
        if orders:
            orders = model_to_dict(orders)
            form = OrderUpdateForm(initial=orders)
            return render(request, 'order/order_update.html', {'form': form, 'order_id': order_id})
        else:
            return render(request, 'maneu/error.html', {'msg': '没有订单'})
    else:
        return render(request, 'maneu/error.html', {'msg': '参数错误'})
