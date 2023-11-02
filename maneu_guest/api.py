import json

from django.http import JsonResponse

from common import common
from maneu_guest import service


def index(request):
    list1 = list(service.ManeuGuess_index(admin_id=request.session.get('id'), star=request.GET.get('star'), end=request.GET.get('end')).values('id', 'name', 'phone', 'time', 'remark'))
    return JsonResponse(list1, safe=False)


def search(request):
    list1 = list(service.ManeuGuess_Search(text=request.GET.get('text'), admin_id=request.session.get('id')).values('id', 'name', 'phone', 'time', 'remark'))
    return JsonResponse(list1, safe=False)


def delete(request):
    service.ManeuGuess_delete(id=request.GET.get('guess_id'))
    return JsonResponse(common.res(), safe=False)
