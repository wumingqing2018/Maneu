from django.shortcuts import render
from django.shortcuts import HttpResponse
from .service import find_order

# Create your views here.


def test_page(request):
    return HttpResponse('test')


def check_order(request, order_id, token):
    order = find_order(order_id, token)
    return render(request, 'guest/check_order.html', {'order': order})
