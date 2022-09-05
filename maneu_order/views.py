from django.forms import model_to_dict
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from common import verify
from maneu_order import service
from maneu_order.forms.orderSearchForm import OrderSearchForm
from maneu_order.forms.orderUpdateForm import OrderUpdateForm
import json


def order_list(request):
    """查看今日订单"""
    orderlist = service.find_order_all()  # 查找今日订单
    return render(request, 'maneu_order/order_list.html', {'orderlist': orderlist})


def order_list_by_guess(request):
    orderlist = service.find_order_all()
    return render(request, 'maneu_order/order_list.html', {'orderlist': orderlist})


def order_delete(request):
    order_id = verify.order_id_method_get(request)
    if order_id:
        order = service.find_order_id(order_id=order_id)
        guess = service.delete_guess_id(id=order.guess_id)
        store = service.delete_store_id(id=order.store_id)
        visionsolutions = service.delete_ManeuVisionSolutions_id(id=order.visionsolutions_id)
        subjectiverefraction = service.delete_subjectiverefraction_id(id=order.subjectiverefraction_id)
        order = service.delete_order_id(id=order_id)
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
        order = service.find_order_id(order_id)
        users = service.find_users_id(id=order.users_id)
        guess = service.find_guess_id(id=order.guess_id)
        store = service.find_store_id(id=order.store_id)
        visionsolutions = service.find_ManeuVisionSolutions_id(id=order.visionsolutions_id)
        subjectiverefraction = service.find_subjectiverefraction_id(id=order.subjectiverefraction_id)
        print(store)
        return render(request, 'maneu_order/order_detail.html',
                      {'order': order, 'users': users, 'guess': guess, 'store': json.loads(store.content),
                       'visionsolutions': json.loads(visionsolutions.content),
                       'subjectiverefraction': json.loads(subjectiverefraction.content)})
    else:
        return render(request, 'maneu/error.html', {'msg': '参数错误'})


def order_detail_v2(request):
    return render(request, 'maneu_order/order_detail_V2.html')


def order_search(request):
    """查找指定订单"""
    phone = verify.phone_method_Post(request)
    if phone:
        orders = service.find_order_phone(phone=phone)  # 查找今日订单
        print(orders)
        return render(request, 'maneu_order/order_list.html', {'orderlist': orders})
    return render(request, 'maneu_order/order_list.html', {'orderlist': ''})


def order_insert(request):
    """添加订单"""
    if request.method == 'POST':
        print(request.POST)
        ManeuVisionSolutions_id = service.ManeuVisionSolutions_insert(VS_remark=request.POST['VS_remark'],
                                                                      OD_BC_DS=request.POST['OD_BC_DS'],
                                                                      OD_BC_CYL=request.POST['OD_BC_CYL'],
                                                                      OD_BC_AX=request.POST['OD_BC_AX'],
                                                                      OD_BC_PR=request.POST['OD_BC_PR'],
                                                                      OD_BC_FR=request.POST['OD_BC_FR'],
                                                                      OD_BC_ADD=request.POST['OD_BC_ADD'],
                                                                      OD_BC_NA=request.POST['OD_BC_NA'],
                                                                      OS_BC_DS=request.POST['OS_BC_DS'],
                                                                      OS_BC_CYL=request.POST['OS_BC_CYL'],
                                                                      OS_BC_AX=request.POST['OS_BC_AX'],
                                                                      OS_BC_PR=request.POST['OS_BC_PR'],
                                                                      OS_BC_FR=request.POST['OS_BC_FR'],
                                                                      OS_BC_ADD=request.POST['OS_BC_ADD'],
                                                                      OS_BC_NA=request.POST['OS_BC_NA']
                                                                      )
        ManeuSubjectiveRefraction_id = service.ManeuSubjectiveRefraction_insert(SR_remark=request.POST['SR_remark'],
                                                                                OD_Nv=request.POST['OD_Nv'],
                                                                                OD_DS=request.POST['OD_DS'],
                                                                                OD_CYL=request.POST['OD_CYL'],
                                                                                OD_AX=request.POST['OD_AX'],
                                                                                OD_NA=request.POST['OD_NA'],
                                                                                OD_AL=request.POST['OD_AL'],
                                                                                OD_AC=request.POST['OD_AC'],
                                                                                OS_Nv=request.POST['OS_Nv'],
                                                                                OS_DS=request.POST['OS_DS'],
                                                                                OS_CYL=request.POST['OS_CYL'],
                                                                                OS_AX=request.POST['OS_AX'],
                                                                                OS_NA=request.POST['OS_NA'],
                                                                                OS_AL=request.POST['OS_AL'],
                                                                                OS_AC=request.POST['OS_AC'],
                                                                                )
        ManeuGuess_id = service.ManeuGuess_insert(name=request.POST['guess_name'], phone=request.POST['guess_phone'],
                                                  sex=request.POST['sex'], age=request.POST['age'],
                                                  OT=request.POST['OT'], EM=request.POST['EM'], DFH=request.POST['DFH'],
                                                  remark=request.POST['remark'])
        ManeuStore_id = service.ManeuStore_insert(arg51=request.POST['arg51'], arg52=request.POST['arg52'],
                                                  arg53=request.POST['arg53'], arg41=request.POST['arg41'],
                                                  arg42=request.POST['arg42'], arg43=request.POST['arg43'],
                                                  arg31=request.POST['arg31'], arg32=request.POST['arg32'],
                                                  arg33=request.POST['arg33'], arg21=request.POST['arg21'],
                                                  arg22=request.POST['arg22'], arg23=request.POST['arg23'],
                                                  arg11=request.POST['arg11'], arg12=request.POST['arg12'],
                                                  arg13=request.POST['arg13'])
        service.ManeuOrderV2_insert(name=request.POST['guess_name'], phone=request.POST['guess_phone'],
                                    users_id=request.session['id'], store_id=ManeuStore_id.id,
                                    guess_id=ManeuGuess_id.id, visionsolutions_id=ManeuVisionSolutions_id.id,
                                    subjectiverefraction_id=ManeuSubjectiveRefraction_id.id, )
        return HttpResponseRedirect(reverse('maneu_order:order_list'))
    return render(request, 'maneu_order/order_insert_v2.html')


def order_update(request):
    """更新订单"""
    order_id = verify.order_id_method_get(request)
    if order_id:
        orders = service.find_order_id(order_id)
        if orders:
            orders = model_to_dict(orders)
            form = OrderUpdateForm(initial=orders)
            return render(request, 'maneu_order/order_update.html', {'form': form, 'order_id': order_id})
        else:
            return render(request, 'maneu/error.html', {'msg': '没有订单'})
    else:
        return render(request, 'maneu/error.html', {'msg': '参数错误'})
