from django.http import JsonResponse

from common.verify import *
from maneu_guest import service


def index(request):
    admin_id = is_uuid(request.session.get('id'))
    start = is_date(request.GET.get('start'))
    end = is_date(request.GET.get('end'))

    if start and end and admin_id:
        try:
            data = service.ManeuGuess_index(admin_id, start, end).values('id', 'name', 'phone', 'time', 'remark')
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
            data = service.ManeuGuess_Search(text=request.GET.get('text'), admin_id=admin_id).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': e, 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def delete(request):
    admin_id = is_uuid(request.session.get('id'))
    guess_id = is_uuid(request.GET.get('id'))

    if admin_id and guess_id:
        try:
            data = service.ManeuGuess_delete(id=guess_id, admin_id=admin_id)
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': e, 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def detail(request):
    admin_id = is_uuid(request.session.get('id'))
    guess_id = is_uuid(request.GET.get('id'))

    if admin_id and guess_id:
        data = service.ManeuGuess_id(id=guess_id, admin_id=admin_id)
        if data:
            content = {'status': True, 'message': '', 'data': data}
        else:
            content = {'status': False, 'message': '没有数据', 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)
