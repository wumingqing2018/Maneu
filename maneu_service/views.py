from django.shortcuts import HttpResponseRedirect, reverse, render, HttpResponse

from maneu_service import service


# Create your views here.


def index(request):
    return render(request, 'maneu_service/index.html',
                  {"list": service.ManeuService_index(admin_id=request.session.get('id'))})


def insert(request):
    if request.method == 'POST':
        service.ManeuService_insert(guess_id=request.POST.get('guess_id'), admin_id=request.session.get('id'),
                                    order_id=request.POST.get('order_id'), content=request.POST.get('content'))
        return HttpResponseRedirect(reverse('maneu_service:index'))
    elif request.method == 'GET':
        order_id = request.GET.get('order_id')
        guess_id = request.GET.get('guess_id')
        return render(request, 'maneu_service/insert.html', {'order_id': order_id, 'guess_id': guess_id})
    else:
        return HttpResponseRedirect(reverse('maneu_service:index'))


def delete(request):
    return HttpResponse(
        service.ManeuService_delete(admin_id=request.session.get('id'), id=request.GET.get('server_id')))


def content(request):
    if request.method == 'POST':
        ManeuService_list = service.ManeuService_orderID(request.POST.get('order_id'))
        return render(request, 'maneu_service/detail.html', {'alterSalesContent': ManeuService_list})
    else:
        return HttpResponseRedirect(reverse('maneu_order:index'))
