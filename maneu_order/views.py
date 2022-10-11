import json

from django.shortcuts import render, reverse, HttpResponseRedirect

from common import common
from common import verify
from common.checkMobile import judge_pc_or_mobile
from maneu_order import service


def order_list(request):
    """查看今日订单"""
    users_id = request.session.get('id')
    orderlist = service.find_order_all(users_id=users_id)  # 查找今日订单
    Datalogs = service.Datalogs_time(users_id=users_id, time=common.month())
    print(Datalogs)
    if Datalogs == None:
        for order in orderlist:
            time = order.time
            month = time.strftime("%m")
            day = time.strftime("%d")
            store_count = 0
            Datalogs = service.Datalogs_time(users_id=users_id, time=month)
            if Datalogs:
                order_logs = json.loads(Datalogs.order_log)
            else:
                order_logs = {"order_log": {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0,
                                            "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0,
                                            "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0,
                                            "31": 0},
                              "order_count": 0,
                              "money_log": {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0,
                                            "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0,
                                            "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0,
                                            "31": 0},
                              "money_count": 0,
                              }
            store_list = ['arg14', 'arg24', 'arg34', 'arg44', 'arg54']
            store_id = order.store_id
            store = json.loads(service.ManeuStore_id(store_id=store_id).content)
            for i in store_list:
                try:
                    store[i] = int(store[i])
                except:
                    store[i] = 0
                store_count = store[i]+store_count
            order_logs["money_log"][day] = order_logs["money_log"][day]+ store_count
            order_logs["order_log"][day] = order_logs["order_log"][day] + 1
            if Datalogs:
                order_logs = service.Datalogs_update(users_id=users_id, time=month,date=time,order_logs=json.dumps(order_logs))
            else:
                order_logs = service.Datalogs_create(users_id=users_id, time=month,date=time,order_logs=json.dumps(order_logs))
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
    order_id = verify.order_id_method_post(request)
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
    return render(request, 'maneu_order/order_detail.html', {'order': order, 'users': users, 'guess': guess,
                                                             'store': json.loads(store.content),
                                                             'visionsolutions': json.loads(visionsolutions.content),
                                                             'subjectiverefraction': json.loads(
                                                                 subjectiverefraction.content)})


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
        print(1,request.POST.get('time'))
        time = json.loads(request.POST.get('time'))['time']
        ManeuGuess_id = service.ManeuGuess_insert(content=request.POST.get('Guess_information'))
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
                                            subjectiverefraction_id=ManeuSubjectiveRefraction_id.id,)
        print(ManeuGuess_id,ManeuStore_id,ManeuVisionSolutions_id,ManeuSubjectiveRefraction_id,order)
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
    print(order_id, users_id)
    if order_id and users_id:
        if request.method == 'GET':
            order = service.find_order_id(order_id=order_id, users_id=users_id)
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


def alterSales_List(request):
    order_id = request.session.get('order_id')
    if order_id:
        return render(request, 'maneu_order/alterSales_list.html',
                      {'alterSalesList': service.ManeuAfterSales_list(order_id=order_id)})
    return HttpResponseRedirect(reverse('maneu_order:order_list'))


def alterSales_content(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        ManeuAfterSales_list = service.ManeuAfterSales_list(order_id)
        return render(request, 'maneu_order/alterSales_content.html', {'alterSalesContent': ManeuAfterSales_list})
    else:
        return HttpResponseRedirect(reverse('maneu_order:order_list'))


def alterSales_insert(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        content = request.POST.get('content')
        insert = service.ManeuAfterSales_insert(content=content, order_id=order_id)
        return HttpResponseRedirect(reverse('maneu_order:alterSalesList'))
    elif request.method == 'GET':
        order_id = request.session.get('order_id')
        return render(request, 'maneu_order/alterSales_insert.html', {'order_id': order_id})
    else:
        return HttpResponseRedirect(reverse('index'))


def alterSales_delete(request):
    if request.method == 'POST':
        insert = service.ManeuAfterSales_delete_id(id=request.POST.get('order_id'))
    return HttpResponseRedirect(reverse('maneu_order:alterSalesList'))

# def datalogs_test(request):
#     users_list = service.find_users_all()
#     print(users_list)
#     for user in users_list:
#         user_id = user.user_id
#         for i in range(1, 31):
#             S = ['2022-09-'+'%02d'%i+' 00:00', '2022-09-'+'%02d'%i+ ' 23:59']
#             order_log = service.find_order_time(time=S, users_id=user_id)
#             if order_log == None:
#                 order_log ='0'
#             print(order_log)
#             service.ManeuDataLogs_insert(user_id=user_id, time='2022-09-'+'%02d'%i, order_log=len(order_log))
#         for i in range(1, 30):
#             S = ['2022-10-'+'%02d'%i+' 00:00', '2022-10-'+'%02d'%i+ ' 23:59']
#             order_log = service.find_order_time(time=S, users_id=user_id)
#             if order_log == None:
#                 order_log ='0'
#             print(order_log)
#             service.ManeuDataLogs_insert(user_id=user_id, time='2022-09-'+'%02d'%i, order_log=len(order_log))
#     return HttpResponseRedirect(reverse('maneu_order:order_list'))
