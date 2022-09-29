import datetime
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
    order_id = verify.order_id_method_get(request)
    users_id = request.session.get('id')
    if order_id and users_id:
        order = service.find_order_id(order_id=order_id, users_id=request.session.get('id'))
        guess = service.delete_guess_id(id=order.guess_id)
        store = service.delete_store_id(id=order.store_id)
        visionsolutions = service.delete_ManeuVisionSolutions_id(id=order.visionsolutions_id)
        subjectiverefraction = service.delete_subjectiverefraction_id(id=order.subjectiverefraction_id)
        order = service.delete_order_id(users_id=request.session.get('id'), id=order_id)
        print(order, guess, store, visionsolutions, subjectiverefraction)
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
    order_id = verify.order_id_method_get(request)
    if order_id:
        order = service.find_order_id(order_id=order_id, users_id=request.session.get('id'))
        users = service.find_users_id(id=order.users_id)
        guess = service.find_guess_id(id=order.guess_id)
        store = service.find_store_id(id=order.store_id)
        visionsolutions = service.find_ManeuVisionSolutions_id(id=order.visionsolutions_id)
        subjectiverefraction = service.find_subjectiverefraction_id(id=order.subjectiverefraction_id)
        return render(request, 'maneu_order/order_detail.html', {'order': order, 'users': users, 'guess': guess,
                                                                 'store': json.loads(store.content),
                                                                 'visionsolutions': json.loads(visionsolutions.content),
                                                                 'subjectiverefraction': json.loads(subjectiverefraction.content)})
    else:
        return render(request, 'maneu/error.html', {'msg': '参数错误'})


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
        guess_content = json.loads(request.POST.get('Guess_information'))
        ManeuGuess_id = service.ManeuGuess_insert(content=request.POST.get('Guess_information'))
        ManeuStore_id = service.ManeuStore_insert(content=request.POST.get('Product_Orders'))
        ManeuVisionSolutions_id = service.ManeuVisionSolutions_insert(content=request.POST.get('Vision_Solutions'))
        ManeuSubjectiveRefraction_id = service.ManeuSubjectiveRefraction_insert(content=request.POST.get('Subjective_refraction'))
        service.ManeuOrderV2_insert(name=guess_content['guess_name'],
                                    phone=guess_content['guess_phone'],
                                    users_id=request.session.get('id'),
                                    store_id=ManeuStore_id.id,
                                    guess_id=ManeuGuess_id.id,
                                    visionsolutions_id=ManeuVisionSolutions_id.id,
                                    subjectiverefraction_id=ManeuSubjectiveRefraction_id.id,)
        return HttpResponseRedirect(reverse('maneu_order:order_list'))
    ua = request.META.get("HTTP_USER_AGENT")
    mobile = judge_pc_or_mobile(ua)
    if mobile:
        return render(request, 'maneu_order/order_insert_V3.html')
    else:
        return render(request, 'maneu_order/order_insert_v2.html')


def order_update(request):
    """更新订单"""
    if request.method == 'GET':
        order_id = verify.order_id_method_get(request)
        if order_id:
            order = service.find_order_id(order_id=order_id, users_id=request.session.get('id'))
            users = service.find_users_id(id=order.users_id)
            guess = service.find_guess_id(id=order.guess_id)
            store = service.find_store_id(id=order.store_id)
            visionsolutions = service.find_ManeuVisionSolutions_id(id=order.visionsolutions_id)
            subjectiverefraction = service.find_subjectiverefraction_id(id=order.subjectiverefraction_id)
            return render(request, 'maneu_order/order_update.html', {'order': order,
                                                                     'users': users,
                                                                     'guess': guess,
                                                                     'store': json.loads(store.content),
                                                                     'visionsolutions': json.loads(
                                                                         visionsolutions.content),
                                                                     'subjectiverefraction': json.loads(
                                                                         subjectiverefraction.content)})
    if request.method == 'POST':
        order_id = verify.order_id_method_post(request)
        if order_id:
            order = service.find_order_id(order_id=order_id, users_id=request.session.get('id'))
            ManeuGuess_id = service.ManeuGuess_update(id=order.guess_id, content=request.POST.get('Guess_information'))
            ManeuStore_id = service.ManeuStore_update(content=request.POST.get('Product_Orders'), id=order.store_id)
            ManeuVisionSolutions_id = service.ManeuVisionSolutions_update(id=order.visionsolutions_id, content=request.POST.get('Vision_Solutions'))
            ManeuSubjectiveRefraction_id = service.ManeuSubjectiveRefraction_update(id=order.subjectiverefraction_id, content=request.POST.get('Subjective_refraction'))
            guess_content = json.loads(request.POST.get('Guess_information'))
            service.ManeuOrderV2_update(order_id=order.id,
                                        name=guess_content['guess_name'],
                                        phone=guess_content['guess_phone'],)
        return HttpResponseRedirect(reverse('maneu_order:order_list'))
    else:
        return render(request, 'maneu/error.html', {'msg': '参数错误'})


def alterSales_List(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        return render(request, 'maneu_order/alterSales_list.html', {'order_id': order_id, 'alterSalesList': service.ManeuAfterSales_list(order_id)})
    else:
        return HttpResponseRedirect(reverse('maneu_order:order_list'))


def alterSales_content(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        print(order_id)
        ManeuAfterSales_list = service.ManeuAfterSales_list(order_id)
        print(ManeuAfterSales_list)
        return render(request, 'maneu_order/alterSales_content.html', {'alterSalesContent': ManeuAfterSales_list})
    else:
        return HttpResponseRedirect(reverse('maneu_order:order_list'))


def alterSales_insert(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        content = request.POST.get('content')
        insert = service.ManeuAfterSales_insert(content=content, order_id=order_id)
        return HttpResponseRedirect(reverse('maneu_order:order_list'))
    elif request.method == 'GET':
        order_id = request.GET.get('order_id')
        return render(request, 'maneu_order/alterSales_insert.html', {'order_id': order_id})
    else:
        return HttpResponseRedirect(reverse('index'))
