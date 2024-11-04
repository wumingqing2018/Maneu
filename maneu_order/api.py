from django.http import JsonResponse

from common import common
from common.verify import is_uuid, is_date
from maneu_order import service
import json

def index(request):
    admin_id = is_uuid(request.session.get('id'))
    start = is_date(request.GET.get('start'))
    end = is_date(request.GET.get('end'))

    if admin_id and start and end:
        try:
            data = service.ManeuOrder_index(admin_id, start, end).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': e, 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def search(request):
    admin_id = is_uuid(request.session.get('id'))

    if admin_id:
        try:
            data = service.ManeuOrder_Search(text=request.GET.get('text'), admin_id=admin_id).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': e, 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def delete(request):
    admin_id = is_uuid(request.session.get('id'))
    order_id = is_uuid(request.GET.get('id'))

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


def insert(request):
    admin_id = is_uuid(request.session.get('id'))
    if admin_id:
        guest_form = json.loads(request.GET.get('guest'))
        guest_id = service.ManeuGuess_search(admin_id=admin_id,
                                             time=request.GET.get('time'),
                                             name=guest_form['name'],
                                             call=guest_form['call'],
                                             sex=guest_form['sex'],
                                             age=guest_form['age'],
                                             ot=guest_form['OT'],
                                             em=guest_form['EM'],
                                             dfh=guest_form['DFH'])[0].id
        if guest_id:
            store_id = service.ManeuStore_insert(admin_id=admin_id,
                                                 guess_id=guest_id,
                                                 time=request.GET.get('time'),
                                                 content=request.GET.get('store')).id
            if store_id:
                order_id = service.ManeuOrder_insert(admin_id=admin_id,
                                                     guess_id=guest_id,
                                                     store_id=store_id,
                                                     time=request.GET.get('time'),
                                                     name=request.GET.get('name'),
                                                     call=request.GET.get('call'),
                                                     remark=request.GET.get('remark')).id
                if order_id:
                    content = {'status': True, 'message': '', 'data': {'id': order_id}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)

def update(request):
    service.ManeuStore_update(id=request.POST.get('store_id'), content=request.POST.get('product_form'))
    service.ManeuOrder_update(id=request.POST.get('order_id'), name=request.POST.get('order_name'),
                              phone=request.POST.get('order_phone'), time=request.POST.get('order_time'),
                              remark=request.POST.get('order_remark'))

def detail(request):
    admin_id = is_uuid(request.session.get('id'))
    order_id = is_uuid(request.GET.get('id'))

    if admin_id and order_id:
        data = service.ManeuOrder_id(id=order_id, admin_id=admin_id)
        if data:
            content = {'status': True, 'message': '', 'data': {'data': data}}
        else:
            content = {'status': False, 'message': '没有数据', 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)
