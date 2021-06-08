from django.http import JsonResponse
from django.forms import model_to_dict

from order.forms.orderInsertForm import OrderInsertForm
from order.forms.orderUpdateForm import OrderUpdateForm
from order import service
from store.service import framework_store

from common import verify
from common import common
import json


def order_list(request):
    """查看今日订单"""
    if request.method == "GET":
        min = verify.is_int(string=request.GET['min'])
        max = verify.is_int(string=request.GET['max'])
        orders = service.find_order_all(min, max).values_list('c_name', 'c_phone', 'c_time')
        res = {'': 0, 'data': list(orders)}
    else:
        res = {'code': 1, 'data': 'request method error'}
    return JsonResponse(res)


def order_insert(request):
    """创建订单"""
    if request.method == "POST":
        form = OrderInsertForm(request.POST)
        if form.is_valid():
            form = form.clean()
            add_order = service.order_insert(form)
            order = json.loads(form['order'])
            for i in order:
                framework_store.framework_count_out(store_id=i['framework'])
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
                res = {'code': 3, 'msg':  '删除失败'}
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


def order_qrcode(request):
    """二维码接口"""
    if request.method == 'POST':
        order_id = verify.is_order_id(request)
        if order_id:
            token = verify.is_order_id(request)
            if token:
                qrcode = common.qrcode(order_id, token)
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


def order_detail(request):
    res = common.res()
    token = verify.verify_order_token_get(request)
    order_id = verify.verify_order_id_get(request)
    if order_id and token:
        res['data'] = model_to_dict(service.find_order_id_and_token(order_id, token))
        res['code'] = 0
    else:
        res['code'] = 1
    return JsonResponse(res)
