from django.shortcuts import render
from common.verify import order_id_method_get
from common.excel import execl_to_json
from maneu_batch.forms.batchInsertForm import BatchInsertForm
from maneu_batch.service import batch


# Create your views here.
def batch_list(request):
    orders = batch.batch_list()
    return render(request, 'batch/batch_list.html', {'orders': orders})


def batch_detail(request):
    # order_id = order_id_method_get(request)
    # if order_id:
    order = batch.batch_detail(request.GET['order_id'])
    return render(request, 'batch/batch_detail.html', {'order': order})


def batch_insert(request):
    if request.method == 'POST':
        form = BatchInsertForm(request.POST)
        execl = execl_to_json(execl=request.FILES.get('execl'))
        if form.is_valid() and execl:
            batch.batch_insert(form.clean(), order=execl)
        else:
            print(1, form.errors)
    return render(request, 'batch/batch_insert.html', {'msg': '参数错误'})
