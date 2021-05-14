from store.models import GlassStore
from common import common


def glass_store_all():
    return GlassStore.objects.all()


def glass_store_id(store_id):
    return GlassStore.objects.filter(store_id=store_id).first()


def glass_store_brand():
    return GlassStore.objects.all()


def glass_store_model(brand):
    return GlassStore.objects.filter(brand=brand).all()


def glass_store_sphere(brand, model):
    try:
        return GlassStore.objects.filter(brand=brand,
                                         model=model).all()
    except BaseException as msg:
        print(msg)
        return None


def glass_store_astigmatic(brand, model, sphere):
    try:
        return GlassStore.objects.filter(brand=brand,
                                         model=model,
                                         sphere=sphere).all()
    except BaseException as msg:
        print(msg)
        return None


def glass_store_refraction(brand, model, sphere, astigmatic):
    try:
        return GlassStore.objects.filter(brand=brand,
                                         model=model,
                                         sphere=sphere,
                                         astigmatic=astigmatic).all()
    except BaseException as msg:
        print(msg)
        return None


def glass_store_count(brand, model, sphere, astigmatic, refraction):
    try:
        return GlassStore.objects.filter(brand=brand,
                                         model=model,
                                         sphere=sphere,
                                         astigmatic=astigmatic,
                                         refraction=refraction).all()
    except BaseException as msg:
        print(msg)
        return None


def glass_store_insert(form):
    try:
        model = GlassStore()
        model.glass_id = common.order_id()
        model.remark = form['remark']
        model.count = form['count']
        model.brand = form['brand']
        model.model = form['model']
        model.sphere = form['sphere']
        model.astigmatic = form['astigmatic']
        model.refraction = form['refraction']
        model.save()
        return model
    except Exception as msg:
        print(msg)
        return None


def glass_store_delete(form):
    try:
        model = GlassStore.objects.filter(id=form.date['id']).all()
        model.delete()
        return True
    except Exception as msg:
        print(msg)
        return False
