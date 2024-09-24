from django.http import JsonResponse

from common import common
from common.verify import *
from maneu_order import service

def index(request):
    admin_id = is_uuid(request.session.get('id'))
    start = is_date(request.GET.get('star'),)
    end = is_date(request.GET.get('end'),)
    res = common.res()

    if admin_id and start and end:
        data = service.ManeuOrder_index(admin_id=request.session.get('id'),
                                        star=request.GET.get('star'),
                                        end=request.GET.get('end')).values('id', 'name', 'phone', 'time', 'remark')
        res['status'] = True
        res['data'] = data
    return JsonResponse(res)


def search(request):
    data = service.ManeuOrder_Search(text=request.GET.get('text'), admin_id=request.session.get('id')).values('id',
                                                                                                              'name',
                                                                                                              'phone',
                                                                                                              'time',
                                                                                                              'remark')
    return JsonResponse(list(data), safe=False)


def delete(request):
    order = service.ManeuOrder_id(id=request.GET.get('order_id'), admin_id=request.session.get('id'))
    if order:
        store = service.ManeuStore_delete(id=order.store_id)
        vision = service.ManeuVision_delete(id=order.vision_id)
        server = service.ManeuService_delete_order_id(order_id=request.GET.get('order_id'))
        order = service.ManeuOrder_delete(admin_id=request.session.get('id'), id=request.GET.get('order_id'))
    return JsonResponse(common.res(), safe=False)


def service_insert(request):
    res = res()
    if request.method == 'POST':
        content = service.ManeuService_insert(guess_id=request.POST.get('guess_id'),
                                              admin_id=request.session.get('id'),
                                              order_id=request.POST.get('order_id'),
                                              content=request.POST.get('content'),
                                              time=common.current_time())
        res['data']['time'] = content.time
        res['data']['content'] = content.content
    return JsonResponse(res)


def service_delete(request):
    res = common.res()
    if request.method == 'POST':
        content = service.ManeuService_delete(admin_id=request.session.get('id'), id=request.POST.get('id'))
        res['data']['content'] = content
    return JsonResponse(res)


def service_update(request):
    res = common.res()
    if request.method == 'POST':
        content = service.ManeuService_update(admin_id=request.session.get('id'), id=request.POST.get('id'),
                                              content=request.POST.get('content'))
        res['data']['content'] = content
    return JsonResponse(res)
