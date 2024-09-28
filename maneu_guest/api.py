from django.http import JsonResponse

from common.verify import *
from maneu.models import ManeuAdmin, ManeuGuess
from maneu_guest import service


def index(request):
    admin_id = is_uuid(request.session.get('id'))
    start = is_date(request.GET.get('star'),)
    end = is_date(request.GET.get('end'),)

    if start and end and admin_id:
        data = service.ManeuGuess_index(admin_id, start, end).values('id', 'name', 'phone', 'time', 'remark')
        content = {'status': True, 'message': '', 'data': list(data)}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def search(request):
    admin_id = is_uuid(request.session.get('id'))

    if admin_id:
        data = service.ManeuGuess_Search(request.GET.get('text'), admin_id).values('id', 'name', 'phone', 'time', 'remark')
        content = {'status': True, 'message': '', 'data': list(data)}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def delete(request):
    admin_id = is_uuid(request.session.get('id'))
    guess_id = is_uuid(request.GET.get('guess_id'))
    if admin_id and guess_id:
        data = service.ManeuGuess_id(admin_id, guess_id)
        content = {'status': True, 'message': '', 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def guestInsert(request):
    ManeuGuess
