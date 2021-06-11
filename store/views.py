from django.shortcuts import render
from django.shortcuts import HttpResponse
from store.service import framework_store
from store.service import glass_store
from common import verify


def store_list(request):
    return render(request, 'store/store.html')


def glass_list(request):
    glass_store_all = glass_store.glass_store_all()
    if glass_store_all:
        return render(request, 'store/glass_list.html', {'glass_list': glass_store_all})
    else:
        return HttpResponse('glass_list_error')


def glass_insert(request):
    return render(request, 'store/glass_insert.html')


def glass_detail(request):
    store_id = verify.verify_store_id_get(request)
    if store_id:
        glass = glass_store.glass_store_id(store_id)
        if glass:
            return render(request, 'store/glass_detail.html', {'glass': glass})


def framework_list(request):
    framework = framework_store.store_all()
    return render(request, 'store/framework_list.html', {'framework_list': framework})


def framework_insert(request):
    return render(request, 'store/framework_insert.html')


def framework_detail(request):
    store_id = verify.verify_store_id_get(request)
    if store_id:
        framework = framework_store.find_store_id(store_id=store_id)
        print(framework['order'])
        return render(request, 'store/framework_detail.html', {'framework': framework})
