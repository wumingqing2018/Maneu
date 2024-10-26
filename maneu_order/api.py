from django.http import JsonResponse

from common import common
from common.verify import *
from maneu_order import service

def index(request):
    admin_id = is_md5(request.session.get('id'))
    start = is_date(request.GET.get('star'))
    end = is_date(request.GET.get('end'))
    print(request.session.get('id'))

    if admin_id:
        data = service.ManeuOrder_index(admin_id=admin_id, star=start, end=end).values('id', 'name', 'phone', 'time', 'remark')
        content = {'status': True, 'message': '', 'data': data}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def search(request):
    admin_id = is_uuid(request.session.get('id'))

    if admin_id:
        data = service.ManeuOrder_Search(text=request.GET.get('text'), admin_id=request.session.get('id'))
        content = {'status': True, 'message': '', 'data': data}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def delete(request):
    admin_id = is_uuid(request.session.get('id'))
    order_id = is_uuid(request.GET.get('order_id'))

    if admin_id and order_id:
        order = service.ManeuOrder_id(id=order_id, admin_id=admin_id)
        if order:
            store = service.ManeuStore_delete(id=order)
            vision = service.ManeuVision_delete(id=order.vision_id)
            server = service.ManeuService_delete_order_id(order_id=request.GET.get('order_id'))
            order = service.ManeuOrder_delete(admin_id=request.session.get('id'), id=request.GET.get('order_id'))
            content = {'status': True, 'message': '', 'data': {}}
        else:
            content = {'status': False, 'message': '请输入正确的参数', 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def service_insert(request):
    admin_id = is_uuid(request.session.get('id'))
    guess_id = is_uuid(request.POST.get('guess_id'))
    order_id = is_uuid(request.POST.get('order_id'))

    if admin_id and guess_id and order_id:
        data = service.ManeuService_insert(guess_id, admin_id, order_id,
                                           content=request.POST.get('content'),
                                           time=common.current_time())
        content = {'status': True, 'message': '', 'data': data}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def service_delete(request):
    admin_id = is_uuid(request.session.get('id'))
    service_id = is_uuid(request.POST.get('id'))

    if admin_id and service_id:
        data = service.ManeuService_delete(admin_id, service_id)
        content = {'status': True, 'message': '', 'data': data}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def service_update(request):
    admin_id = is_uuid(request.session.get('id'))
    service_id = is_uuid(request.POST.get('id'))

    if admin_id and service_id:
        data = service.ManeuService_update(admin_id, service_id, request.POST.get('content'))
        content = {'status': True, 'message': '', 'data': data}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)