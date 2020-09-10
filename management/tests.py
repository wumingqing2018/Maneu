from django.test import TestCase
from django.shortcuts import render
from management.models import ProductManage

from management.my_lib import *
from management.service import *

import time
import random
# Create your tests here.
def test(request):

    orders = ProductManage.objects.create(
        id=creste_order_id(),
        c_time=current_time(),
        c_name='1',
        c_phone='13640651582',
        u_time=current_time(),
        u_name='1',
        u_phone='13640615582',
    )
    return HttpResponse(orders)

def guest_page(request):
    order = guest_find_order(id='2020071416520397', token='1')
    return render(request, 'guest_order_page.html', {'order': order})


def update_time(request):
    orders = ProductManage.objects.all()
    for order in orders:
        order.c_time = current_day()
        order.save()
    return HttpResponse('OK')