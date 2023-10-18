import json
from common import common

from django.shortcuts import render

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
        order = json.loads(request.POST.get('order_json'))
        ManeuGuess_id = service.ManeuGuess_search(admin_id=request.session.get('id'),
                                                  time=order['time'],
                                                  name=order['name'],
                                                  phone=order['phone'],
                                                  sex=order['sex'],
                                                  age=order['age'],
                                                  ot=order['OT'],
                                                  em=order['EM'],
                                                  dfh=order['DFH'])[0].id

        vision_id = service.ManeuVision_insert(admin_id=request.session.get('id'), guess_id=ManeuGuess_id,
                                               time=order['time'], content=request.POST.get('Vision_Solutions')).id
        store_id = service.ManeuStore_insert(admin_id=request.session.get('id'), guess_id=ManeuGuess_id,
                                             time=order['time'], content=request.POST.get('Product_Orders')).id
        order_id = service.ManeuOrder_insert(time=order['time'], name=order['name'], phone=order['phone'],
                                             admin_id=request.session.get('id'),
                                             guess_id=ManeuGuess_id,
                                             store_id=store_id,
                                             vision_id=vision_id).id
        request.POST._mutable = True
        request.POST['order_id'] = order_id
        request.POST._mutable = False
        return detail(request)
    time = common.today()
    return render(request, 'maneu_order/insert.html', {'time': time})


def update(request):
    """更新订单"""
    if request.method == 'GET':
        content = {}
        content['order'] = service.ManeuOrder_id(id=request.GET.get('order_id'), admin_id=request.session.get('id'))
        content['store'] = service.ManeuStore_id(id=content['order'].store_id)
        content['vision'] = service.ManeuVision_id(id=content['order'].vision_id)
        return render(request, 'maneu_order/update.html', content)
    if request.method == 'POST':
        order = json.loads(request.POST.get('order_json'))
        service.ManeuVision_update(id=request.POST.get('vision_id'),
                                   content=request.POST.get('Vision_Solutions'))
        service.ManeuStore_update(id=request.POST.get('store_id'), content=request.POST.get('Product_Orders'))
        service.ManeuOrder_update(order_id=request.POST.get('order_id'), name=order['name'], phone=order['phone'])
        return detail(request)
    return index(request)


