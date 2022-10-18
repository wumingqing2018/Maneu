import json

from django.shortcuts import render, reverse, HttpResponseRedirect

from common import verify
from common.checkMobile import judge_pc_or_mobile
from maneu_order import service


def order_list(request):
    """查看今日订单"""
    orderlist = service.find_order_all(users_id=request.session.get('id'))  # 查找今日订单
    return render(request, 'maneu_order/order_list.html', {'orderlist': orderlist})


def order_delete(request):
    order_id = request.session.get('order_id')
    users_id = request.session.get('id')
    if order_id and users_id:
        order = service.find_order_id(order_id=order_id, users_id=users_id)
        guess = service.delete_guess_id(id=order.guess_id)
        store = service.delete_store_id(id=order.store_id)
        visionsolutions = service.delete_ManeuVisionSolutions_id(id=order.visionsolutions_id)
        subjectiverefraction = service.delete_subjectiverefraction_id(id=order.subjectiverefraction_id)
        order = service.delete_order_id(users_id=users_id, id=order_id)
        afterSales = service.ManeuAfterSales_delete(order_id=order_id)
    return HttpResponseRedirect(reverse('maneu_order:order_list'))


def order_detail(request):
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
        order_id = request.session.get('order_id')
        if order_id == None:
            return render(request, 'maneu/error.html', {'msg': '参数错误'})
    request.session['order_id'] = order_id
    order = service.find_order_id(order_id=order_id, users_id=request.session.get('id'))
    users = service.find_users_id(id=order.users_id)
    guess = service.find_guess_id(id=order.guess_id)
    store = service.find_store_id(id=order.store_id)
    visionsolutions = service.find_ManeuVisionSolutions_id(id=order.visionsolutions_id)
    subjectiverefraction = service.find_subjectiverefraction_id(id=order.subjectiverefraction_id)
    return render(request, 'maneu_order/order_detail.html', {'maneu_order': order, 'users': users, 'guess': guess,
                                                             'maneu_store': json.loads(store.content),
                                                             'visionsolutions': json.loads(visionsolutions.content),
                                                             'subjectiverefraction': json.loads(subjectiverefraction.content)})


def order_search(request):
    if request.method == 'POST':
        """查找指定订单"""
        orderlist = service.find_ManeuOrderV2_search(date=request.POST.get('date'), text=request.POST.get('text'),
                                                     users_id=request.session.get('id'))
        return render(request, 'maneu_order/order_list.html', {'orderlist': orderlist})
    return HttpResponseRedirect(reverse('maneu_order:order_list'))


def order_insert(request):
    """添加订单"""
    if request.method == 'POST':
        time = json.loads(request.POST.get('time'))['time']
        ManeuGuess_id = service.ManeuGuess_insert(content=request.POST.get('Guess_information'))
        print(ManeuGuess_id)
        ManeuStore_id = service.ManeuStore_insert(content=request.POST.get('Product_Orders'))
        ManeuVisionSolutions_id = service.ManeuVisionSolutions_insert(content=request.POST.get('Vision_Solutions'))
        ManeuSubjectiveRefraction_id = service.ManeuSubjectiveRefraction_insert(content=request.POST.get('Subjective_refraction'))
        order = service.ManeuOrderV2_insert(name=ManeuGuess_id.name,
                                            phone=ManeuGuess_id.phone,
                                            users_id=request.session.get('id'),
                                            store_id=ManeuStore_id.id,
                                            guess_id=ManeuGuess_id.id,
                                            time=time,
                                            visionsolutions_id=ManeuVisionSolutions_id.id,
                                            subjectiverefraction_id=ManeuSubjectiveRefraction_id.id, )
        if order:
            request.session['order_id'] = str(order.id)
            return HttpResponseRedirect(reverse('maneu_order:order_detail'))
    ua = request.META.get("HTTP_USER_AGENT")
    mobile = judge_pc_or_mobile(ua)
    if mobile:
        return render(request, 'maneu_order/order_insert_V3.html')
    else:
        return render(request, 'maneu_order/order_insert_v2.html')


def order_update(request):
    """更新订单"""
    order_id = request.session.get('order_id')
    users_id = request.session.get('id')
    if order_id and users_id:
        if request.method == 'GET':
            order = service.find_order_id(order_id=order_id, users_id=users_id)
            users = service.find_users_id(id=order.users_id)
            guess = service.find_guess_id(id=order.guess_id)
            store = service.find_store_id(id=order.store_id)
            visionsolutions = service.find_ManeuVisionSolutions_id(id=order.visionsolutions_id)
            subjectiverefraction = service.find_subjectiverefraction_id(id=order.subjectiverefraction_id)
            return render(request, 'maneu_order/order_update.html', {'maneu_order': order,
                                                                     'users': users,
                                                                     'guess': guess,
                                                                     'maneu_store': json.loads(store.content),
                                                                     'visionsolutions': json.loads(
                                                                         visionsolutions.content),
                                                                     'subjectiverefraction': json.loads(
                                                                         subjectiverefraction.content)})
        if request.method == 'POST':
            order = service.find_order_id(order_id=order_id, users_id=users_id)
            ManeuGuess_id = service.ManeuGuess_update(id=order.guess_id, content=request.POST.get('Guess_information'))
            ManeuStore_id = service.ManeuStore_update(content=request.POST.get('Product_Orders'), id=order.store_id)
            ManeuVisionSolutions_id = service.ManeuVisionSolutions_update(id=order.visionsolutions_id,
                                                                          content=request.POST.get('Vision_Solutions'))
            ManeuSubjectiveRefraction_id = service.ManeuSubjectiveRefraction_update(id=order.subjectiverefraction_id,
                                                                                    content=request.POST.get(
                                                                                        'Subjective_refraction'))
            guess_content = json.loads(request.POST.get('Guess_information'))
            service.ManeuOrderV2_update(order_id=order.id,
                                        name=guess_content['guess_name'],
                                        phone=guess_content['guess_phone'], )
            return HttpResponseRedirect(reverse('maneu_order:order_detail'))

    return render(request, 'maneu/error.html', {'msg': '参数错误'})
