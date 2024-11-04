import json

from django.shortcuts import render

from common.common import current_time
from maneu_order import service


def index(request):
    """
    订单列表功能
    在session获取商家id 通过商家id查找订单列表
    """
    return render(request, 'maneu_order/index.html')


def detail(request):
    """
    查看订单详情
    校验请求模式 GET 校验order_id是否符合
    true
        渲染order_detail页面并传输参数order_id
    false
        渲染error页面并传输错误参数
    """
    order_id = request.POST.get('order_id')
    if order_id == None:
        order_id = request.GET.get('order_id')
    order = service.ManeuOrder_id(id=order_id, admin_id=request.session.get('id'))
    guess = service.ManeuGuess_id(id=order.guess_id)
    store = service.ManeuStore_id(id=order.store_id).content
    vision = service.ManeuVision_id(id=order.vision_id).content
    server = service.ManeuService_orderID(order_id=order.id)
    return render(request, 'maneu_order/detail.html',{'order': order, 'store': store, 'vision': vision, 'server': server, 'guess': guess})


def insert(request):
    """添加订单"""
    return render(request, 'maneu_order/insert.html', {'time': current_time()})


def update(request):
    """更新订单"""
    id = request.GET.get('id')
    return render(request, 'maneu_order/update.html', {'id':id})
