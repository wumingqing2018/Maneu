import json

from django.shortcuts import render

from common import common
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
    return render(request, 'maneu_order/detail.html', {'order': order, 'store': store, 'vision': vision, 'server': server, 'guess': guess})


def insert(request):
    """添加订单"""
    if request.method == 'POST':
        guess_form = json.loads(request.POST.get('guess_form'))
        guess_id = service.ManeuGuess_search(admin_id=request.session.get('id'), time=request.POST.get('order_time'), name=guess_form['name'], phone=guess_form['phone'], sex=guess_form['sex'], age=guess_form['age'], ot=guess_form['OT'], em=guess_form['EM'], dfh=guess_form['DFH'])[0].id
        vision_id = service.ManeuVision_insert(admin_id=request.session.get('id'), guess_id=guess_id, time=request.POST.get('order_time'), content=request.POST.get('vision_form')).id
        store_id = service.ManeuStore_insert(admin_id=request.session.get('id'), guess_id=guess_id, time=request.POST.get('order_time'), content=request.POST.get('product_form')).id
        order_id = service.ManeuOrder_insert(time=request.POST.get('order_time'), name=request.POST.get('order_name'), phone=request.POST.get('order_phone'), remark=request.POST.get('order_remark'), admin_id=request.session.get('id'), guess_id=guess_id, store_id=store_id, vision_id=vision_id).id
        request.POST._mutable = True
        request.POST['order_id'] = order_id
        request.POST._mutable = False
        return detail(request)
    return render(request, 'maneu_order/insert.html', {'time': common.current_time()})


def update(request):
    """更新订单"""
    if request.method == 'GET':
        order = service.ManeuOrder_id(id=request.GET.get('order_id'), admin_id=request.session.get('id'))
        content = {"order": order,
                   "guess": service.ManeuGuess_id(id=order.guess_id),
                   "store": json.loads(service.ManeuStore_id(id=order.store_id).content),
                   "vision": json.loads(service.ManeuVision_id(id=order.vision_id).content)}
        return render(request, 'maneu_order/update.html', content)
    if request.method == 'POST':
        print(request.POST)
        service.ManeuVision_update(id=request.POST.get('vision_id'), content=request.POST.get('vision_form'))
        service.ManeuStore_update(id=request.POST.get('store_id'), content=request.POST.get('product_form'))
        service.ManeuGuess_update(id=request.POST.get('guess_id'), content=request.POST.get('guess_form'))
        service.ManeuOrder_update(id=request.POST.get('order_id'), name=request.POST.get('order_name'), phone=request.POST.get('order_phone'), time=request.POST.get('order_time'), remark=request.POST.get('order_remark'))
        return detail(request)
    return index(request)
