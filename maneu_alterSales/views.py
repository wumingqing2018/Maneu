from django.shortcuts import HttpResponseRedirect, reverse, render
from common import common
from maneu_alterSales import service
import datetime

# Create your views here.
def list(request):
    order_id = request.session.get('order_id')
    if order_id:
        return render(request, 'maneu_afterSales/list.html', {'alterSalesList': service.ManeuAfterSales_orderID(order_id=order_id)})
    return HttpResponseRedirect(reverse('maneu_order:index'))


def index(request):
    if request.GET.get('time'):
        time = request.GET.get('time')
    else:
        time = common.today()
    date = datetime.datetime.strptime(time, '%Y-%m-%d')
    down_day = (date + datetime.timedelta(days=+1)).strftime("%Y-%m-%d")
    up_day = (date + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    list = service.ManeuAfterSales_index(time=time)  # 查找今日订单
    return render(request, 'maneu_afterSales/index.html', {'list': list,
                                                      'time': time,
                                                      'up_day': up_day,
                                                      'down_day': down_day})


def content(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        ManeuAfterSales_list = service.ManeuAfterSales_orderID(order_id)
        return render(request, 'maneu_afterSales/detail.html', {'alterSalesContent': ManeuAfterSales_list})
    else:
        return HttpResponseRedirect(reverse('maneu_order:index'))


def insert(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        content = request.POST.get('content')
        insert = service.ManeuAfterSales_insert(content=content, order_id=order_id)
        return HttpResponseRedirect(reverse('maneu_alterSales:alterSalesList'))
    elif request.method == 'GET':
        order_id = request.session.get('order_id')
        return render(request, 'maneu_afterSales/insert.html', {'order_id': order_id})
    else:
        return HttpResponseRedirect(reverse('index'))


def delete(request):
    if request.method == 'POST':
        insert = service.ManeuAfterSales_delete_id(id=request.POST.get('order_id'))
    return HttpResponseRedirect(reverse('maneu_alterSales:alterSalesList'))
