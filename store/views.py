from django.shortcuts import render

from common import verify
from store.service import framework_store
from store.service import glass_store


def store_list(request):
    return render(request, 'store/store_list.html')


def glass_list(request):
    glass_store_all = glass_store.glass_store_all()
    return render(request, 'store/glass_list.html', {'glass_list': glass_store_all})


def glass_insert(request):
    return render(request, 'store/glass_insert.html')


def glass_detail(request):
    store_id = verify.store_id_method_get(request)
    if store_id:
        glass = glass_store.glass_store_id(store_id)
        if glass:
            return render(request, 'store/glass_detail.html', {'glass': glass})
        else:
            return render(request, 'maneu/error.html', {'msg': '没有订单'})
    else:
        return render(request, 'maneu/error.html', {'msg': '参数错误'})


def framework_list(request):
    framework = framework_store.store_all()
    return render(request, 'store/framework_list.html', {'framework_list': framework})


def framework_insert(request):
    return render(request, 'store/framework_insert.html')


def framework_detail(request):
    store_id = verify.store_id_method_get(request)
    if store_id:
        framework = framework_store.find_store_id(store_id=store_id)
        return render(request, 'store/framework_detail.html', {'framework': framework})
    else:
        return render(request, 'maneu/error.html', {'msg': '参数错误'})
