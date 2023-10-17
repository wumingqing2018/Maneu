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


def delete(request):
    content = {}
    return JsonResponse(content)
