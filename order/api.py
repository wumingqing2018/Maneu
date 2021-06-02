from django.http import JsonResponse

from .forms.orderInsertForm import OrderInsertForm
from .forms.orderUpdateForm import OrderUpdateForm
from . import service

from common import verify
from common import common


def order_list(request):
    """查看今日订单"""
    if request.method == "GET":
        min = verify.is_int(string=request.GET['min'])
        max = verify.is_int(string=request.GET['max'])
        orders = service.find_order_all(min, max).values_list('c_name', 'c_phone', 'c_time')
        res = {'code': 0, 'data': list(orders)}
    else:
        res = {'code': 1, 'data': 'request method error'}
    return JsonResponse(res)


def order_insert(request):
    """创建订单"""
    print(request.POST)
    if request.method == "POST":
        form = OrderInsertForm(request.POST)
        if form.is_valid():
            add_order = service.order_insert(form=form.clean())
            if add_order:
                res = {'code': 0, 'msg': '创建成功'}
            else:
                res = {'code': 3, 'msg': '创建失败'}
        else:
            res = {'code': 2, 'msg': form.errors}
    else:
        res = {'code': 1, 'msg': '请求出错'}
    return JsonResponse(res)


def order_delete(request):
    """删除订单"""
    if request.method == 'POST':
        order_id = verify.is_order_id(request)
        if order_id:
            delete = service.order_delete(order_id)
            if delete:
                res = {'code': 0, 'msg': '删除成功'}
            else:
                res = {'code': 3, 'msg': '删除失败'}
        else:
            res = {'code': 2, 'msg': '请求参数出错'}
    else:
        res = {'code': 1, 'msg': '请求方式出错'}
    return JsonResponse(res)


def order_update(request):
    """更新订单"""
    if request.method == 'POST':
        order_id = verify.is_order_id(request)
        if order_id:
            form = OrderUpdateForm(request.POST)
            if form.is_valid():
                update = service.order_update(order_id, form)
                if update:
                    res = {'code': 0, 'msg': '更新成功'}
                else:
                    res = {'code': 4, 'msg': '更新失败'}
            else:
                res = {'code': 3, 'msg': form.errors}
        else:
            res = {'code': 2, 'msg': '参数出错'}
    else:
        res = {'code': 1, 'msg': '请求出错'}
    return JsonResponse(res)


def qr_code(request):
    """二维码接口"""
    if request.method == 'POST':
        order_id = verify.is_order_id(request)
        if order_id:
            token = verify.is_order_id(request)
            if token:
                qrcode = common.qrcode_api(order_id, token)
                if qrcode:
                    res = {'code': 0, 'msg': '生成成功'}
                else:
                    res = {'code': 4, 'msg': '生成失败'}
            else:
                res = {'code': 3, 'msg': '参数2出错'}
        else:
            res = {'code': 2, 'msg': '参数1出错'}
    else:
        res = {'code': 1, 'msg': '请求出错'}
    return JsonResponse(res)
