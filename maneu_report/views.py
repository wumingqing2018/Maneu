from django.shortcuts import render

from common.common import current_time


def index(request):
    """
    订单列表功能
    在session获取商家id 通过商家id查找订单列表
    """
    return render(request, 'maneu_report/index.html')


def insert(request):
    """添加订单"""
    return render(request, 'maneu_report/insert.html', {'time': current_time()})


def update(request):
    """更新订单"""
    id = request.GET.get('id')
    return render(request, 'maneu_report/update.html', {'order_id': id})


def detail(request):
    id = request.GET.get('id')
    return render(request, 'maneu_report/detail.html', {'order_id': id})
