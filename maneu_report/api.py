from django.http import JsonResponse

from common import common
from common.verify import is_uuid, is_date
from maneu_order import service
import json


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
