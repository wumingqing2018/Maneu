from django.forms import model_to_dict
from django.http import JsonResponse

from common import common
from common.verify import is_uuid, is_date
from maneu_order import service
import json


def detail(request):
    order_id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))

    if admin_id and order_id:
        try:
            data = model_to_dict(service.ManeuOrder_id(id=order_id, admin_id=admin_id))
            content = {'status': True, 'message': '', 'data': data}
        except Exception as e:
            content = {'status': False, 'message': e, 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)
