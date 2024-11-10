from django.forms import model_to_dict
from django.shortcuts import render

from common.common import current_time
from common.verify import is_uuid

from maneu_order import service

def index(request):
    """
    订单列表功能
    在session获取商家id 通过商家id查找订单列表
    """
    return render(request, 'maneu_order/index.html')


def insert(request):
    """添加订单"""
    return render(request, 'maneu_order/insert.html', {'time': current_time()})


def update(request):
    """更新订单"""
    id = request.GET.get('id')
    return render(request, 'maneu_order/update.html', {'order_id': id})


def detail(request):
    """
    查看订单详情
    校验请求模式 GET 校验order_id是否符合
    true
        渲染order_detail页面并传输参数order_id
    false
        渲染error页面并传输错误参数
    """
    id = request.GET.get('id')
    return render(request, 'maneu_order/detail.html', {'order_id': id})
