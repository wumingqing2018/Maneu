from django.forms import model_to_dict
from django.http import JsonResponse

from common.verify import is_uuid,is_date
from maneu_guest import service


def index(request):
    admin_id = is_uuid(request.session.get('id'))
    start = is_date(request.GET.get('start'))
    end = is_date(request.GET.get('end'))

    if start and end and admin_id:
        try:
            data = service.ManeuGuest_index(admin_id, start, end).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def search(request):
    admin_id = is_uuid(request.session.get('id'))

    if admin_id:
        try:
            data = service.ManeuGuest_Search(text=request.GET.get('text'), admin_id=admin_id).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def insert(request):
    admin_id = is_uuid(request.session.get('id'))

    if admin_id:
        try:
            data = service.ManeuGuest_insert(admin_id=admin_id,
                                             time=request.GET.get('time'),
                                             name=request.GET.get('name'),
                                             phone=request.GET.get('call'),
                                             sex=request.GET.get('sex'),
                                             age=request.GET.get('age'),
                                             dfh=request.GET.get('dfh'),
                                             ot=request.GET.get('ot'),
                                             em=request.GET.get('em'),
                                             remark=request.GET.get('remark'))
            content = {'status': True, 'message': '', 'data': data[0].id}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def delete(request):
    admin_id = is_uuid(request.session.get('id'))
    guest_id = is_uuid(request.GET.get('id'))

    if admin_id and guest_id:
        try:
            data = service.ManeuGuest_delete(id=guest_id, admin_id=admin_id)
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def detail(request):
    guest_id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))

    if admin_id and guest_id:
        try:
            data = service.ManeuGuest_detail(id=guest_id, admin_id=admin_id)
            content = {'status': True, 'message': '', 'data': model_to_dict(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def update(request):
    guest_id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))

    if admin_id and guest_id:
        try:
            data = service.ManeuGuest_update(id=guest_id,
                                             admin_id=admin_id,
                                             phone=request.GET.get('call'),
                                             time=request.GET.get('time'),
                                             name=request.GET.get('name'),
                                             sex=request.GET.get('sex'),
                                             age=request.GET.get('age'),
                                             ot=request.GET.get('ot'),
                                             em=request.GET.get('em'),
                                             dfh=request.GET.get('dfh'),
                                             remark=request.GET.get('remark'))
            content = {'status': True, 'message': '', 'data':{}}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)