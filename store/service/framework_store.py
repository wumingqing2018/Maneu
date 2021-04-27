from store.models import FrameworkStore
from common.common import order_id


def framework_store_insert(form):
    try:
        model = FrameworkStore()
        model.store_id = order_id()
        model.brand = form['brand']
        model.model = form['model']
        model.remark = form['model']
        model.save()
        return model
    except BaseException as msg:
        print(msg)
        return None


def framework_store_brand():
    try:
        return FrameworkStore.objects.all()
    except BaseException as msg:
        print(msg)
        return None


def framework_store_model(brand):
    try:
        return FrameworkStore.objects.filter(brand=brand).all()
    except BaseException as msg:
        print(msg)
        return None


def framework_store_count(brand, model):
    try:
        return FrameworkStore.objects.filter(brand=brand, model=model).first()
    except BaseException as msg:
        print(msg)
        return None
