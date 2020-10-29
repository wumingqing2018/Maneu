from django.shortcuts import render
from django.shortcuts import HttpResponse
from .service import guest_find_order

# Create your views here.


def test_page(request):
    return HttpResponse('1')


def check_order(request, order_id, token):
    order = guest_find_order(order_id, token)
    return HttpResponse(order)
