import json

from django.forms import model_to_dict
from django.http import JsonResponse

from common import common
from common import verify
from maneu_order import service
from maneu_order.forms.orderInsertForm import OrderInsertForm
from maneu_order.forms.orderUpdateForm import OrderUpdateForm
from maneu_store.service import framework_store
from maneu_store.service import glass_store


def order_list(request):
    """查看今日订单"""
    if request.method == "GET":
        PageNumber = verify.is_int(string=request.GET['PageNumber'])
        orders = service.find_order_today(PageNumber).values_list('c_name', 'c_phone', 'c_time')
        res = {'code': 0, 'msg': '', 'data': list(orders)}
    else:
        res = {'code': 1, 'msg': "request method error", 'data': []}
    return JsonResponse(res)


def order_insert(request):
    """创建订单"""
    if request.method == "POST":
        form = OrderInsertForm(request.POST)
        if form.is_valid():
            form = form.clean()
            add_order = service.order_insert(form)
            order = json.loads(form['maneu_order'])
            for i in order:
                if i['product'] == "镜框":
                    framework_store.framework_count_out(store_id=i['store_id'])
                elif i['product'] == "镜片":
                    glass_store.glass_count_out(store_id=i['store_id'])
            if add_order:
                res = {'code': 0, 'msg': '创建成功', 'data': []}
            else:
                res = {'code': 3, 'msg': '创建失败', 'data': []}
        else:
            res = {'code': 2, 'msg': form.errors, 'data': []}
    else:
        res = {'code': 1, 'msg': "请求出错", 'data': []}
    return JsonResponse(res)


def order_delete(request):
    """删除订单"""
    if request.method == 'POST':
        order_id = verify.order_id_method_post(request)
        if order_id:
            delete = service.order_delete(order_id)
            if delete:
                res = {'code': 0, 'msg': '删除成功', 'data': []}
            else:
                res = {'code': 3, 'msg':  '删除失败', 'data': []}
        else:
            res = {'code': 2, 'msg': '请求参数出错', 'data': []}
    else:
        res = {'code': 1, 'msg': '请求方式出错', 'data': []}
    return JsonResponse(res)


def order_update(request):
    """更新订单"""
    if request.method == 'POST':
        order_id = verify.order_id_method_post(request)
        if order_id:
            form = OrderUpdateForm(request.POST)
            if form.is_valid():
                update = service.order_update(order_id, form)
                if update:
                    res = {'code': 0, 'msg': '更新成功', 'data': []}
                else:
                    res = {'code': 4, 'msg': '更新失败', 'data': []}
            else:
                res = {'code': 3, 'msg': form.errors, 'data': []}
        else:
            res = {'code': 2, 'msg': '参数出错', 'data': []}
    else:
        res = {'code': 1, 'msg': '请求出错', 'data': []}
    return JsonResponse(res)


def order_qrcode(request):
    """二维码接口"""
    if request.method == 'POST':
        order_id = verify.order_id_method_post(request)
        order_token = verify.order_token_method_post(request)
        if order_id and order_token:
            qrcode = common.make_qrcode(order_id=order_id, order_token=order_token)
            if qrcode:
                res = {'code': 0, 'msg': '生成成功', 'data': []}
            else:
                res = {'code': 3, 'msg': '生成失败', 'data': []}
        else:
            res = {'code': 2, 'msg': '参数出错', 'data': []}
    else:
        res = {'code': 1, 'msg': '请求出错', 'data': []}
    return JsonResponse(res)


def order_detail(request):
    order_id = verify.order_id_method_get(request)
    if order_id:
        res = {'code': 0, 'msg': '', 'data': [model_to_dict(service.find_order_id(order_id))]}
    else:
        res = {'code': 1, 'msg': '参数错误', 'data': []}
    return JsonResponse(res)
