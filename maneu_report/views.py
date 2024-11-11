from django.shortcuts import render
from common.common import current_time


def index(request):
    return render(request, 'maneu_report/index.html')


def insert(request):
    return render(request, 'maneu_report/insert.html', {'time': current_time()})


def update(request):
    return render(request, 'maneu_report/update.html', {'id': request.GET.get('id')})


def detail(request):
    return render(request, 'maneu_report/detail.html', {'id': request.GET.get('id')})
