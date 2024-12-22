from django.http import JsonResponse

from common.verify import is_uuid
from maneu_order import service


def insert(request):
    admin_id = is_uuid(request.session.get('id'))
    guest_id = is_uuid(request.GET.get('guest_id'))

    if admin_id and guest_id:
        try:
            store = service.ManeuStore_insert(admin_id=admin_id, guest_id=guest_id, time=request.GET.get('time'), content=request.GET.get('store'))
            content = {'status': True, 'message': '', 'data': {'id': store.id}}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)
