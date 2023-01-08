from django.shortcuts import render, HttpResponseRedirect, reverse
from guess import service
import json
# Create your views here.


def order_list(request):
    orderList = service.find_order_GuessId(guessId=request.session.get('id'))
    return render(request, 'guess/orderList.html', {'orderlist': orderList})


def order_detail(request):
    order_id = request.POST.get('order_id')
    if type(order_id) == str:
        order = service.find_order_Id(orderID=order_id)
        if order != None:
            guess = service.find_guess_id(id=order.guess_id)
            users = service.find_users_id(id=order.users_id)
            store = service.find_store_id(id=order.store_id)
            visionsolutions = service.find_ManeuVisionSolutions_id(id=order.visionsolutions_id)
            return render(request, 'guess/orderDetail.html', {'users': users,
                                                               'guess': guess,
                                                               'store': json.loads(store.content),
                                                               'visionsolutions': json.loads(visionsolutions.content),
                                                               })
    return HttpResponseRedirect(reverse('guess_admin:order_list'))
