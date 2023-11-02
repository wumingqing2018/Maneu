from common import common

from django.http import JsonResponse

from maneu_order import service


def index(request):
    list1 = list(service.ManeuOrder_index(admin_id=request.session.get('id'), star=request.GET.get('star'), end=request.GET.get('end')).values('id', 'name', 'phone', 'time', 'remark'))
    return JsonResponse(list1, safe=False)


def search(request):
    list1 = list(service.ManeuOrder_Search(text=request.GET.get('text'), admin_id=request.session.get('id')).values('id', 'name', 'phone', 'time', 'remark'))
    return JsonResponse(list1, safe=False)


def delete(request):
    order = service.ManeuOrder_id(id=request.GET.get('order_id'), admin_id=request.session.get('id'))
    if order:
        store = service.ManeuStore_delete(id=order.store_id)
        vision = service.ManeuVision_delete(id=order.vision_id)
        server = service.ManeuService_delete_order_id(order_id=request.GET.get('order_id'))
        order = service.ManeuOrder_delete(admin_id=request.session.get('id'), id=request.GET.get('order_id'))
    return JsonResponse(common.res(), safe=False)


def service_insert(request):
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


def service_insert(request):
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

