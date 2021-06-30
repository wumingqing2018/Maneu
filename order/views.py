from django.shortcuts import render
from django.shortcuts import HttpResponse
from order import service
from common import verify


def order_list(request):
    """查看今日订单"""
    orders = service.find_order_all()  # 查找今日订单
    return render(request, 'order/order_list.html', {'orders': orders})


def order_detail(request):
    """查看订单详情"""
    order_id = verify.order_id_method_get(request)
    if order_id:
        orders = service.find_order_id(order_id)
        if orders:
            return render(request, 'order/order_detail.html', {'order_id': orders.order_id,
                                                               'order_token': orders.order_token})
        else:
            return HttpResponse('error: 2')
    else:
        return HttpResponse('error: 1')


def order_search(request):
    """查找指定订单"""
    from .forms.orderSearchForm import OrderSearchForm
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
    from .forms.orderUpdateForm import OrderUpdateForm
    from django.forms import model_to_dict

    order_id = verify.order_id_method_get(request)
    if order_id:
        orders = service.find_order_id(order_id)
        if orders:
            orders = model_to_dict(orders)
            form = OrderUpdateForm(initial=orders)
            return render(request, 'order/order_update.html', {'form': form, 'order_id': order_id})
        else:
            return HttpResponse('error: 2')
    else:
        return HttpResponse('error: 1')
