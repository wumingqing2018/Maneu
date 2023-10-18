import json

from django.http import JsonResponse

from maneu_order import service


def reference(request):
    guess_id = service.ManeuGuess_phone('').id
    content = json.loads(service.ManeuRefraction_id(guess_id).content)
    return JsonResponse(content)


def index(request):
    list1 = list(service.ManeuOrder_index(admin_id=request.session.get('id'), star=request.GET.get('star'), end=request.GET.get('end')).values('id', 'name', 'phone', 'time'))  # 查找今日订单
    return JsonResponse(list1, safe=False)


def search(request):
    list1 = list(service.ManeuOrder_Search(text=request.GET.get('text'), admin_id=request.session.get('id')).values('id', 'name', 'phone', 'time'))
    return JsonResponse(list1, safe=False)


def delete(request):
    order = service.ManeuOrder_id(id=request.GET.get('order_id'), admin_id=request.session.get('id'))
    if order:
        store = service.ManeuStore_delete(id=order.store_id)
        vision = service.ManeuVision_delete(id=order.vision_id)
        server = service.ManeuService_delete_order_id(order_id=request.GET.get('order_id'))
        order = service.ManeuOrder_delete(admin_id=request.session.get('id'), id=request.GET.get('order_id'))
    list1 = list({'type': True})
    return JsonResponse(list1, safe=False)

