from django.http import JsonResponse
from common import common
from maneu_service import service


# Create your views here.


def index(request):
    content = list(service.ManeuService_index(admin_id=request.session.get('id')).values())
    return JsonResponse(content)


def insert(request):
    res = common.res()
    if request.method == 'POST':
        content = service.ManeuService_insert(guess_id=request.POST.get('guess_id'),
                                              admin_id=request.session.get('id'),
                                              order_id=request.POST.get('order_id'),
                                              content=request.POST.get('content'),
                                              time=common.current_time())
        res['data']['time'] = content.time
        res['data']['content'] = content.content
    return JsonResponse(res)


def delete(request):
    content = service.ManeuService_delete(admin_id=request.session.get('id'), id=request.GET.get('server_id'))
    return JsonResponse(content)
