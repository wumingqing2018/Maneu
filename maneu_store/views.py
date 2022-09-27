from django.shortcuts import render
from maneu_store import service


def store_insert(request):
    return render(request, 'maneu_store/store_insert.html')


def store_list(request):
    store_list = service.store_item_all()
    return render(request, 'maneu_store/store_list.html', {'store_list': store_list})


def glass_insert(request):
    return render(request, 'maneu_store/glass_insert.html')
