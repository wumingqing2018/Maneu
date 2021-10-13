from django.shortcuts import render

from common import verify
from maneu_store.service import store


def store_insert(request):
    return render(request, 'maneu_store/store_insert.html')


def store_list(request):
    return render(request, 'maneu_store/store_list.html')


def glass_insert(request):
    return render(request, 'maneu_store/glass_insert.html')
