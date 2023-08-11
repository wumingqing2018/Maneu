import json

from django.http import JsonResponse

from common import common
from maneu_service import service


# Create your tests here.


def insert(request):
    if request.method == 'POST':
        content = json.loads(request.POST.get('content'))
        insert = service.ManeuService_insert(time=common.today(), guess_id=content['guess_id'],
                                             admin_id=request.session.get('id'), order_id=content['order_id'],
                                             content=content['content'])
        return JsonResponse({'code': '0', 'msg': 'success',
                             'data': {'server_id': insert.id, 'time': insert.time, 'content': insert.content}})
    return JsonResponse({'code': '1', 'msg': 'method error', 'data': {}})
