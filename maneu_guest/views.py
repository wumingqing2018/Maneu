from django.shortcuts import render
from common.common import current_time


def index(request):
    return render(request, 'maneu_guest/index.html')


def insert(request):
    return render(request, 'maneu_guest/insert.html', {'time': current_time()})


def detail(request):
    return render(request, 'maneu_guest/detail.html',{'id': request.GET.get('id')})