import json

from django.forms import model_to_dict
from django.http import JsonResponse

from common.simple import order_simple
from common.verify import is_uuid, is_date
from maneu_order import service


def index(request):
    admin_id = is_uuid(request.session.get('id'))
    start = is_date(request.GET.get('start'))
    end = is_date(request.GET.get('end'))

    if admin_id and start and end:
        try:
            data = service.order_index(admin_id, start, end).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': admin_id, 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '参数错误请确认', 'data': {}}

    return JsonResponse(content)


def search(request):
    admin_id = is_uuid(request.session.get('id'))

    if admin_id:
        try:
            data = service.order_search(text=request.GET.get('text'), admin_id=admin_id).values('id', 'name', 'phone',
                                                                                                'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '参数错误请确认', 'data': {}}

    return JsonResponse(content)


def insert(request):
    admin_id = is_uuid(request.session.get('id'))
    guest_id = is_uuid(request.GET.get('guest_id'))
    report_id = is_uuid(request.GET.get('report_id'))

    if admin_id and guest_id and report_id:
        try:
            content = order_simple(request.GET.get('content'))
            order = service.order_insert(admin_id=admin_id,
                                         guest_id=guest_id,
                                         report_id=report_id,
                                         time=request.GET.get('time'),
                                         name=request.GET.get('name'),
                                         call=request.GET.get('call'),
                                         content=content,
                                         remark=request.GET.get('remark'))
            content = {'status': True, 'message': '', 'data': {'id': order.id}}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '参数错误请确认', 'data': {}}

    return JsonResponse(content)


def update(request):
    admin_id = is_uuid(request.session.get('id'))
    order_id = is_uuid(request.GET.get('order_id'))

    if admin_id and order_id:
        try:
            content = order_simple(request.GET.get('content'))
            order = service.order_update(admin_id=admin_id,
                                         order_id=order_id,
                                         time=request.GET.get('time'),
                                         name=request.GET.get('name'),
                                         call=request.GET.get('call'),
                                         content=content,
                                         remark=request.GET.get('remark'))
            content = {'status': True, 'message': '', 'data': {'id': order.id}}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '参数错误请确认', 'data': {}}

    return JsonResponse(content)


def detail(request):
    order_id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))

    if admin_id and order_id:
        try:
            order = service.order_id(order_id=order_id, admin_id=admin_id)
            content = {
                'content': json.loads(order.content),
                'guest_id': order.guest_id,
                'report_id': order.report_id,
                'name': order.name,
                'phone': order.phone,
                'remark': order.remark,
                'time': order.time
            }
            content = {'status': True, 'message': '', 'data': content}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def delete(request):
    order_id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))

    if admin_id and order_id:
        try:
            order = service.order_id(order_id=order_id, admin_id=admin_id)
            report = service.report_delete(report_id=order.report_id, admin_id=admin_id)
            order = service.order_delete(order_id=order_id, admin_id=admin_id)
            content = {'status': True, 'message': '', 'data': {}}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)
