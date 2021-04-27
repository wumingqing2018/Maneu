from django.shortcuts import render
from .service import framework_store
from .service import glass_store


def store(request):
    return render(request, 'store/store.html')


def glass_store_all(request):
    glass_list = glass_store.glass_store_all()
    return render(request, 'store/glass_store.html', {'glass_list': glass_list})


def glass_content(request):
    glass_list = glass_store.glass_store_id(glass_id=request.GET['glass_id'])
    return render(request, 'store/glass.html', {'glass_list': glass_list})


def glass_insert(request):
    return render(request, 'store/glass_insert.html')


def framework_list(request):
    return render(request, 'store/frame_store.html')


def framework_find(request):
    find = framework_store.framework_store_find_brand_model()
    print(find)
    return render(request, 'store/frame_store.html')


def framework_insert(request):
    return render(request, 'store/framework_insert.html')
