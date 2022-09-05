from os import name
from django.shortcuts import render

from maneu_class import service


def class_list(request):
    return render(request, 'maneu_class/class_list.html', {'classList': service.class_list()})


def class_insert(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'maneu_class/class_insert.html')