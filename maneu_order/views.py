from django.shortcuts import render
from common.common import current_time


def index(request):
    return render(request, 'maneu_order/index.html')


def insert(request):
    return render(request, 'maneu_order/insert.html', {'time': current_time()})


def detail(request):
    return render(request, 'maneu_order/detail.html', {'order_id': request.GET.get('id')})
