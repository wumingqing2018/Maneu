from django.http import JsonResponse
from store.service import glass_store
from store.service import framework_store
from store.forms.glass_store_insert import GlassStoreInsert
from store.forms.frame_store_insert import FrameStoreInsert
from common import verify


def glass_insert(request):
    if request.method == 'POST':
        form = GlassStoreInsert(request.POST)
        if form.is_valid():
            insert = glass_store.glass_store_insert(form=form.clean())
            if insert:
                res = {'code': 0, 'msg': 'save succeed', 'data': []}
            else:
                res = {'code': 3, 'msg': 'save failed', 'data': []}
        else:
            res = {'code': 2, 'msg': form.errors}
    else:
        res = {'code': 1, 'msg': 'request method error'}
    return JsonResponse(res)


def glass_brand(request):
    if request.method == 'GET':
        brand = glass_store.glass_store_all().values_list('brand').distinct()
        res = {'code': 0, 'msg': 'request succeed', 'data': list(brand)}
    else:
        res = {'code': 1, 'msg': 'request failed', 'data': []}
    return JsonResponse(res)


def glass_model(request):
    if request.method == 'GET':
        try:
            brand = request.GET['brand']
        except BaseException as msg:
            print(msg)
            brand = ''
        model = glass_store.glass_store_model(brand=brand).values_list('model').distinct()
        res = {'code': 0, 'msg': 'request succeed', 'data': list(model)}
    else:
        res = {'code': 1, 'msg': 'request failed', 'data': []}
    return JsonResponse(res)


def glass_sphere(request):
    if request.method == 'GET':
        try:
            brand = request.GET['brand']
            model = request.GET['model']
        except BaseException as msg:
            print(msg)
            brand = ''
            model = ''
        sphere = glass_store.glass_store_sphere(brand, model).values_list('sphere').distinct()
        res = {'code': 0, 'msg': 'request succeed', 'data': list(sphere)}
    else:
        res = {'code': 1, 'msg': 'request failed', 'data': []}
    return JsonResponse(res)


def glass_astigmatic(request):
    if request.method == 'GET':
        try:
            brand = request.GET['brand']
            model = request.GET['model']
            sphere = request.GET['sphere']
        except BaseException as msg:
            print(msg)
            brand = ''
            model = ''
            sphere = ''
        astigmatic = glass_store.glass_store_astigmatic(brand=brand, model=model, sphere=sphere).values_list('astigmatic').distinct()
        res = {'code': 0, 'msg': 'request succeed', 'data': list(astigmatic)}
    else:
        res = {'code': 1, 'msg': 'request failed', 'data': []}
    return JsonResponse(res)


def glass_refraction(request):
    if request.method == 'GET':
        try:
            brand = request.GET['brand']
            model = request.GET['model']
            sphere = request.GET['sphere']
            astigmatic = request.GET['astigmatic']
        except BaseException as msg:
            print(msg)
            brand = ''
            model = ''
            sphere = ''
            astigmatic = ''
        refraction = glass_store.glass_store_refraction(brand, model, sphere, astigmatic).values_list('refraction').distinct()
        res = {'code': 0, 'msg': 'request succeed', 'data': list(refraction)}
    else:
        res = {'code': 1, 'msg': 'request failed', 'data': []}
    return JsonResponse(res)


def glass_count(request):
    if request.method == 'GET':
        try:
            brand = request.GET['brand']
            model = request.GET['model']
            sphere = request.GET['sphere']
            astigmatic = request.GET['astigmatic']
            refraction = request.GET['refraction']
        except BaseException as msg:
            print(msg)
            brand = ''
            model = ''
            sphere = ''
            astigmatic = ''
            refraction = ''
        store_id = glass_store.glass_store_count(brand, model, sphere, astigmatic, refraction).values_list('store_id', 'count').distinct()
        res = {'code': 0, 'msg': 'request succeed', 'data': list(store_id)}
    else:
        res = {'code': 1, 'msg': 'request failed', 'data': []}
    return JsonResponse(res)


def framework_brand(request):
    if request.method == 'GET':
        brand = framework_store.framework_store_brand().values_list('brand').distinct()
        res = {'code': 0, 'msg': 'request succeed', 'data': list(brand)}
    else:
        res = {'code': 1, 'msg': 'request failed', 'data': []}
    return JsonResponse(res)


def framework_model(request):
    if request.method == 'GET':
        try:
            brand = request.GET['brand']
        except BaseException as msg:
            print(msg)
            brand = ''
        model = framework_store.framework_store_model(brand=brand).values_list('model').distinct()
        res = {'code': 0, 'msg': 'request succeed', 'data': list(model)}
    else:
        res = {'code': 1, 'msg': 'request failed', 'data': []}
    return JsonResponse(res)


def framework_count(request):
    if request.method == 'GET':
        try:
            brand = request.GET['brand']
            model = request.GET['model']
        except BaseException as msg:
            print(msg)
            brand = ''
            model = ''
        store_id = framework_store.framework_store_count(brand=brand, model=model).store_id
        res = {'code': 0, 'msg': 'request succeed', 'data': store_id}
    else:
        res = {'code': 1, 'msg': 'request failed', 'data': ''}
    return JsonResponse(res)


def framework_insert(request):
    if request.method == 'POST':
        form = FrameStoreInsert(request.POST)
        if form.is_valid():
            insert = framework_store.framework_store_insert(form=form.clean())
            if insert:
                res = {'code': 0, 'msg': 'save succeed'}
                return JsonResponse(res)
            else:
                res = {'code': 3, 'msg': 'save failed'}
                return JsonResponse(res)
        else:
            res = {'code': 2, 'msg': form.errors}
            return JsonResponse(res)
    else:
        res = {'code': 1, 'msg': 'request method error'}
        return JsonResponse(res)
