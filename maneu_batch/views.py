from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse

from common import common
from common.excel import excel_save
from common import verify
from maneu_batch import service
from maneu_batch.forms.BatchInsertForm import BatchInsertForm


# Create your views here.
def batch_list(request):
    orderlist = service.batch_list()
    return render(request, 'maneu_batch/batch_list.html', {'orderlist': orderlist})


def batch_list_ByName(request):
    print(request.GET['arg'])
    orders = service.batch_list_ByName(arg=request.GET['arg'])
    return render(request, 'maneu_batch/batch_list.html', {'orders': orders})


def batch_list_ByPhone(request):
    print(request.GET['arg'])
    orders = service.batch_list_ByPhone(arg=request.GET['arg'])
    return render(request, 'maneu_batch/batch_list.html', {'orders': orders})


def batch_detail(request):

    order_id = verify.order_id_method_get(request)
    if order_id:
        order = service.batch_detail(order_id)
        return render(request, 'maneu_batch/batch_detail.html', {'order': order})
    else:
        return render(request, 'maneu/error.html', {'msg': '参数错误'})


def batch_delete(request):
    order_id = order_id_method_get(request)
    if order_id:
        print(service.batch_delete(order_id))
        # excel_remove(order_id)
        return batch_list(request)
    else:
        return render(request, 'maneu/error.html')


def batch_insert(request):
    msg = None
    if request.method == 'POST':
        form = BatchInsertForm(request.POST)
        excel = request.FILES.get('excel')
        if form.is_valid() and excel:
            order_id = create_id()
            order = excel_save(excel, order_id)
            service.batch_insert(form.clean(), order, order_id)
            return batch_list(request)
        msg = '参数错误'
    return render(request, 'maneu_batch/batch_insert.html', {'msg': msg})


def batch_search(request):
    """查找指定订单"""
    date = verify.date_method_post(request)
    if date:
        orderlist = service.find_batch_date(date=date)  # 查找今日订单
        return render(request, 'maneu_batch/batch_list.html', {'orderlist': orderlist})
    return HttpResponseRedirect(reverse('maneu_order:order_list'))
