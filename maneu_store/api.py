from django.http import JsonResponse

from maneu_store.service import store


def item_list(request):
    item = list(store.store_item_all())
    return JsonResponse(item)
