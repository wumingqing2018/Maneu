from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse
from maneu_alterSales import service

# Create your views here.
def alterSales_List(request):
    order_id = request.session.get('order_id')
    if order_id:
        return render(request, 'maneu_afterSales/alterSales_list.html', {'alterSalesList': service.ManeuAfterSales_list(order_id=order_id)})
    return HttpResponseRedirect(reverse('maneu_order:order_list'))


def alterSalesindex(request):
    return render(request, 'maneu_afterSales/afterSales_index.html', {'alterSalesList': service.ManeuAfterSales_index()})


def alterSales_content(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        ManeuAfterSales_list = service.ManeuAfterSales_list(order_id)
        return render(request, 'maneu_afterSales/alterSales_content.html', {'alterSalesContent': ManeuAfterSales_list})
    else:
        return HttpResponseRedirect(reverse('maneu_order:order_list'))


def alterSales_insert(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        content = request.POST.get('content')
        insert = service.ManeuAfterSales_insert(content=content, order_id=order_id)
        return HttpResponseRedirect(reverse('maneu_alterSales:alterSalesList'))
    elif request.method == 'GET':
        order_id = request.session.get('order_id')
        return render(request, 'maneu_afterSales/alterSales_insert.html', {'order_id': order_id})
    else:
        return HttpResponseRedirect(reverse('index'))


def alterSales_delete(request):
    if request.method == 'POST':
        insert = service.ManeuAfterSales_delete_id(id=request.POST.get('order_id'))
    return HttpResponseRedirect(reverse('maneu_order:alterSalesList'))
