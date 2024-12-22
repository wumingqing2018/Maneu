import json

from django.forms import model_to_dict
from django.http import JsonResponse

from common.common import current_time
from common.verify import is_uuid, is_date
from maneu_order import service


def index(request):
    admin_id = is_uuid(request.session.get('id'))
    start = is_date(request.GET.get('start'))
    end = is_date(request.GET.get('end'))

    if admin_id and start and end:
        try:
            data = service.ManeuOrder_index(admin_id, start, end).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': admin_id, 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': admin_id, 'data': {}}
    else:
        content = {'status': False, 'message': admin_id, 'data': {}}

    return JsonResponse(content)


def search(request):
    admin_id = is_uuid(request.session.get('id'))

    if admin_id:
        try:
            data = service.ManeuOrder_Search(text=request.GET.get('text'), admin_id=admin_id).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def delete(request):
    order_id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))

    if admin_id and order_id:
        order = service.ManeuOrder_id(id=order_id, admin_id=admin_id)
        if order:
            store = service.ManeuStore_delete(id=order.store_id)
            print(store)
            vision = service.ManeuVision_delete(id=order.vision_id)
            print(vision)
            server = service.ManeuService_delete_order_id(order_id=order.id)
            print(server)
            order = service.ManeuOrder_delete(admin_id=request.session.get('id'), id=request.GET.get('order_id'))
            print(order)
            content = {'status': True, 'message': '', 'data': {}}
        else:
            content = {'status': False, 'message': '请输入order的参数', 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def service_insert(request):
    admin_id = is_uuid(request.session.get('id'))
    guest_id = is_uuid(request.POST.get('guest_id'))
    order_id = is_uuid(request.POST.get('order_id'))

    if admin_id and guest_id and order_id:
        data = service.ManeuService_insert(guest_id, admin_id, order_id,
                                           content=request.POST.get('content'),
                                           time=current_time())
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


def insert(request):
    admin_id = is_uuid(request.session.get('id'))
    store_id = is_uuid(request.GET.get('store_id'))
    guest_id = is_uuid(request.GET.get('guest_id'))
    report_id = is_uuid(request.GET.get('report_id'))

    if admin_id and store_id and guest_id and report_id:
        try:
            order = service.ManeuOrder_insert(admin_id=admin_id,
                                              guest_id=guest_id,
                                              store_id=store_id,
                                              report_id = report_id,
                                              time=request.GET.get('time'),
                                              name=request.GET.get('name'),
                                              call=request.GET.get('call'),
                                              remark=request.GET.get('remark'))
            content = {'status': True, 'message': '', 'data': {'id': order.id}}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def update(request):
    service.ManeuStore_update(id=request.POST.get('store_id'), content=request.POST.get('product_form'))
    service.ManeuOrder_update(id=request.POST.get('order_id'), name=request.POST.get('order_name'),
                              phone=request.POST.get('order_phone'), time=request.POST.get('order_time'),
                              remark=request.POST.get('order_remark'))


def detail(request):
    order_id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))

    if admin_id and order_id:
        try:
            data = service.ManeuOrder_id(id=order_id, admin_id=admin_id)
            content = {'status': True, 'message': '', 'data': model_to_dict(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)
