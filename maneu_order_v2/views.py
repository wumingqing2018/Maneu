import json
from datetime import datetime

from django.shortcuts import render

from maneu_order_v2 import service


def search(request):
    time = request.GET.get('time')
    text = request.GET.get('text')
    admin_id = request.session.get('id')
    if text:
        """查找指定订单"""
        list = service.ManeuOrderV2_Search(text=text, admin_id=admin_id)
        return render(request, 'maneu_order_v2/index.html', {'list': list})
    elif time:
        list = service.ManeuOrderV2_time(time=datetime.strptime(time, "%Y-%m-%d"), admin_id=admin_id)
        return render(request, 'maneu_order_v2/index.html', {'list': list})
    return index(request)


def index(request):
    """
    订单列表功能
    在session获取商家id 通过商家id查找订单列表
    """
    list = service.ManeuOrderV2_all(admin_id=request.session.get('id'))  # 查找今日订单
    return render(request, 'maneu_order_v2/index.html', {'list': list})


def delete(request):
    # order = service.ManeuOrderV2_id(id=request.POST.get('order_id'), admin_id=request.session.get('id'))
    # if order:
    #     store = service.ManeuStore_delete(id=order.store_id)
    #     vision = service.ManeuVisionSolutions_delete(id=order.visionsolutions_id)
    #     server = service.ManeuService_delete_order_id(order_id=request.POST.get('order_id'))
    #     order = service.ManeuOrderV2_delete(admin_id=request.session.get('id'), id=request.POST.get('order_id'))
    service.ManeuOrderV2_delete(admin_id=request.session.get('id'), id=request.POST.get('order_id'))
    return index(request)


def detail(request):
    """
    查看订单详情
    校验请求模式 GET 校验order_id是否符合
    true
        渲染order_detail页面并传输参数order_id
    false
        渲染error页面并传输错误参数
    """
    content = {}
    content['order'] = service.ManeuOrderV2_id(id=request.POST.get('order_id'), admin_id=request.session.get('id'))
    content['store'] = service.ManeuStore_id(id=content['order'].store_id).content
    content['vision'] = service.ManeuVisionSolutions_id(id=content['order'].visionsolutions_id).content
    content['server'] = service.ManeuService_orderID(order_id=content['order'].id)
    return render(request, 'maneu_order_v2/detail.html', content)


def insert(request):
    """添加订单"""
    if request.method == 'POST':
        order = json.loads(request.POST.get('order_json'))
        try:
            ManeuGuess_id = service.ManeuGuess_search(admin_id=request.session.get('id'), name=order['name'], phone=order['phone']).id
        except:
            ManeuGuess_id = service.ManeuGuess_insert(admin_id=request.session.get('id'), name=order['name'], phone=order['phone'], time=order['time']).id
        vision_id = service.ManeuVisionSolutions_insert(admin_id=request.session.get('id'), guess_id=ManeuGuess_id, time=order['time'], content=request.POST.get('Vision_Solutions')).id
        store_id = service.ManeuStore_insert(admin_id=request.session.get('id'), guess_id=ManeuGuess_id, time=order['time'], content=request.POST.get('Product_Orders')).id
        order_id = service.ManeuOrderV2_insert(time=order['time'], name=order['name'], phone=order['phone'],
                                               admin_id=request.session.get('id'),
                                               guess_id=ManeuGuess_id,
                                               store_id=store_id,
                                               visionsolutions_id=vision_id).id
        request.POST._mutable = True
        request.POST['order_id'] = order_id
        request.POST._mutable = False
        return detail(request)
    return render(request, 'maneu_order_v2/insert.html')


def update(request):
    """更新订单"""
    if request.method == 'GET':
        content= {}
        content['order'] = service.ManeuOrderV2_id(id=request.GET.get('order_id'), admin_id=request.session.get('id'))
        content['store'] = service.ManeuStore_id(id=content['order'].store_id)
        content['vision'] = service.ManeuVisionSolutions_id(id=content['order'].visionsolutions_id)
        return render(request, 'maneu_order_v2/update.html', content)
    if request.method == 'POST':
        order = json.loads(request.POST.get('order_json'))
        service.ManeuVisionSolutions_update(id=request.POST.get('vision_id'), content=request.POST.get('Vision_Solutions'))
        service.ManeuStore_update(id=request.POST.get('store_id'), content=request.POST.get('Product_Orders'))
        service.ManeuOrderV2_update(order_id=request.POST.get('order_id'), name=order['name'], phone=order['phone'])
        return detail(request)
    return index(request)


def test1(request):
    print()