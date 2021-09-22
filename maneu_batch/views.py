from os import remove
from django.shortcuts import render
from common.verify import order_id_method_get
from common.common import create_id
from common.excel import excel_save
from common.excel import excel_remove

from maneu_batch import service
from maneu_batch.forms.batchInsertForm import BatchInsertForm


# Create your views here.
def batch_list(request):
    orders = service.batch_list()
    return render(request, 'batch/batch_list.html', {'orders': orders})


def batch_insert(request):
    msg = 'None'
    if request.method == 'POST':
        form = BatchInsertForm(request.POST)
        excel = request.FILES.get('excel')
        if form.is_valid() and excel:
            order_id = create_id()
            order = excel_save(excel, order_id)
            if order:
                service.batch_insert(form.clean(), order, order_id)
            else:
                msg = 'excel格式错误'
        else:
            msg = "检查用户姓名和电话格式是否正确"
    return render(request, 'batch/batch_insert.html', {'msg': msg})


def batch_delete(request):
    order_id = order_id_method_get(request)
    if order_id:
        service.batch_delete(order_id)
        excel_remove(order_id)
        orders = service.batch_list()
        return render(request, 'batch/batch_list.html', {'orders': orders})


def batch_detail(request):
    order_id = order_id_method_get(request)
    if order_id:
        order = service.batch_detail(order_id)
        return render(request, 'batch/batch_detail.html',  {'order': order})
