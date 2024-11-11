from django.forms import model_to_dict
from django.http import JsonResponse

from common.common import current_time
from common.verify import is_uuid, is_date
from maneu_report import service


def index(request):
    admin_id = is_uuid(request.session.get('id'))
    start = is_date(request.GET.get('start'))
    end = is_date(request.GET.get('end'))

    if admin_id and start and end:
        try:
            data = service.report_index(admin_id, start, end).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def search(request):
    admin_id = is_uuid(request.session.get('id'))
    text = request.GET.get('text')
    if admin_id:
        try:
            data = service.report_search(text=text, admin_id=admin_id).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def delete(request):
    id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))

    if admin_id and id:
        try:
            data = service.report_delete(admin_id, id)
            content = {'status': True, 'message': '', 'data': {}}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def insert(request):
    print(request.GET)
    admin_id = is_uuid(request.session.get('id'))

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
