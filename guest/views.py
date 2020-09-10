from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def test_page(request):
    return HttpResponse('1')


def check_order(request, id, token,):
    return HttpResponse(id)