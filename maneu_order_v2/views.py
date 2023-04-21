import json

from django.shortcuts import render, reverse, HttpResponseRedirect

from common import checkMobile
from maneu_order_v2 import service


def index(request):
    """
    订单列表功能
    在session获取商家id 通过商家id查找订单列表
    """
    list = service.ManeuOrderV2_all(admin_id=request.session.get('id'))  # 查找今日订单
    return render(request, 'maneu_order_v2/index.html', {'list': list})


def delete(request):
    order = service.ManeuOrderV2_id(id=request.POST.get('id'), admin_id=request.session.get('id'))
    if order:
        store = service.ManeuStore_delete(id=order.store_id)
        vision = service.ManeuVisionSolutions_delete(id=order.visionsolutions_id)
        server = service.ManeuService_delete_order_id(order_id=request.POST.get('id'))
        order = service.ManeuOrderV2_delete(admin_id=request.session.get('id'), id=request.POST.get('id'))
    return HttpResponseRedirect(reverse('maneu_order_v2:index'))


def detail(request):
    """
    查看订单详情
    校验请求模式 GET 校验order_id是否符合
    true
        渲染order_detail页面并传输参数order_id
    false
        渲染error页面并传输错误参数
    """
    try:
        order_id = request.POST['id']
        request.session['order_id'] = order_id
    except:
        order_id = request.session.get('order_id')
    order = service.ManeuOrderV2_id(id=order_id, admin_id=request.session.get('id'))
    if order:
        content = {}
        content['order'] = order
        content['guess'] = service.ManeuGuess_id(id=order.guess_id)
        content['store'] = service.ManeuStore_id(id=order.store_id)
        content['vision'] = service.ManeuVisionSolutions_id(id=order.visionsolutions_id)
        return render(request, 'maneu_order_v2/detail_pc.html', content)
    return HttpResponseRedirect(reverse('maneu_order_v2:index'))


def search(request):
    time = request.GET.get('time')
    text = request.GET.get('text')
    admin_id = request.session.get('id')
    if text:
        """查找指定订单"""
        list = service.ManeuOrderV2_Search(text=text, admin_id=admin_id)
        return render(request, 'maneu_order_v2/index.html', {'list': list})
    elif time:
        list = service.ManeuOrderV2_time(time=time, admin_id=admin_id)
        return render(request, 'maneu_order_v2/index.html', {'list': list})
    return HttpResponseRedirect(reverse('maneu_order_v2:index'))


def insert(request):
    """添加订单"""
    if request.method == 'POST':
        order = json.loads(request.POST.get('order_json'))
        try:
            ManeuGuess_id = service.ManeuGuess_search(admin_id=request.session.get('id'), name=order['name'], phone=order['phone']).id
        except:
            ManeuGuess_id = service.ManeuGuess_insert(admin_id=request.session.get('id'), name=order['name'], phone=order['phone']).id
        store_id = service.ManeuStore_insert(time=order['time'], content=request.POST.get('Product_Orders')).id
        vision_id = service.ManeuVisionSolutions_insert(time=order['time'], content=request.POST.get('Vision_Solutions')).id
        request.session['order_id'] = str(service.ManeuOrderV2_insert(time=order['time'], name=order['name'], phone=order['phone'], admin_id=request.session.get('id'), guess_id=ManeuGuess_id, store_id=store_id, visionsolutions_id=vision_id).id)
        return HttpResponseRedirect(reverse('maneu_order_v2:detail'))
    if checkMobile.judge_pc_or_mobile(ua=request.META.get("HTTP_USER_AGENT")):
        return render(request, 'maneu_order_v2/insert_phone.html')
    else:
        return render(request, 'maneu_order_v2/insert_pc.html')


def update(request):
    """更新订单"""
    order_id = request.session.get('order_id')
    admin_id = request.session.get('id')
    if order_id and admin_id:
        if request.method == 'GET':
            order = service.ManeuOrderV2_id(order_id=order_id, admin_id=admin_id)
            users = service.admin_id(id=order.admin_id)
            guess = service.guess_id(id=order.guess_id)
            store = service.ManeuStore_id(id=order.ManeuStore_id)
            return render(request, 'maneu_order_v2/update.html', {'maneu_order_v2': order, 'users': users, 'guess': guess,
                                                                  # 'maneu_store': json.loads(store.content),
                                                                  })
        if request.method == 'POST':
            order = service.ManeuOrderV2_id(order_id=order_id, admin_id=admin_id)
            ManeuGuess_id = service.ManeuGuess_update(id=order.guess_id, content=request.POST.get('Guess_information'))
            ManeuStore_id = service.ManeuStore_update(content=request.POST.get('Product_Orders'), id=order.ManeuStore_id)
            guess_content = json.loads(request.POST.get('Guess_information'))
            service.ManeuOrderV2_update(order_id=order.id,name=guess_content['guess_name'],phone=guess_content['guess_phone'], )
            return HttpResponseRedirect(reverse('maneu_order_v2:detail'))
    return HttpResponseRedirect(reverse('maneu_order_v2:update'))


def test1(request):
    store_list = service.ManeuStore.objects.exclude(orderid='').all()

    for store in store_list:
        try:
            print(service.ManeuOrderV2.objects.filter(id=store.orderid).update(store_id=store.id))
        except Exception as e:
            print(e)


def test2(request):
    store_list = service.ManeuVisionSolutions.objects.exclude(orderid='').all()
    for store in store_list:
        try:
            print(service.ManeuOrderV2.objects.filter(id=store.orderid).update(visionsolutions_id=store.id))
        except Exception as e:
            print(e)