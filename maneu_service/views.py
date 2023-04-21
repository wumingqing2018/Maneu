from django.shortcuts import HttpResponseRedirect, reverse, render
from common import common
from maneu_service import service
import datetime
# Create your views here.


def index1(request):
    list = service.ManeuService_index1(admin_id=request.session.get('id'))  # 查找今日订单
    return render(request, 'maneu_service/index.html', {'list': list})


def index2(request):
    list = service.ManeuService_index2(order_id=request.POST.get('id'))  # 查找今日订单
    return render(request, 'maneu_service/index.html', {'list': list})


def index3(request):
    list = service.ManeuService_index3(guess_id=request.POST.get('guess_id'))  # 查找今日订单
    return render(request, 'maneu_service/index.html', {'list': list})


def insert(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        content = request.POST.get('content')
        insert = service.ManeuService_insert(content=content, order_id=order_id)
        return HttpResponseRedirect(reverse('maneu_service:alterSalesList'))
    elif request.method == 'GET':
        order_id = request.session.get('order_id')
        print(order_id)
        return render(request, 'maneu_service/insert.html', {'order_id': order_id})
    else:
        return HttpResponseRedirect(reverse('index'))


def delete(request):
    insert = service.ManeuService_delete_id(id=request.POST.get('id'))
    return HttpResponseRedirect(reverse('maneu_service:index1'))


def content(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        ManeuService_list = service.ManeuService_orderID(order_id)
        return render(request, 'maneu_service/detail.html', {'alterSalesContent': ManeuService_list})
    else:
        return HttpResponseRedirect(reverse('maneu_order_v2:index'))
