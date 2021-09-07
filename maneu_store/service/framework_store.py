from common import common
from store.models import FrameworkStore


def store_all():
    return FrameworkStore.objects.all()


def find_store_id(store_id):
    return FrameworkStore.objects.filter(store_id=store_id).first()


def framework_store_insert(form):
    try:
        model = FrameworkStore()
        model.store_id = common.order_id()
        model.brand = form['brand']
        model.model = form['model']
        model.count = form['count']
        model.remark = form['remark']
        model.time = common.current_time()

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


def framework_count_out(store_id, count=1):
    try:
        model = FrameworkStore.objects.filter(store_id=store_id).first()
        model.count = int(model.count)-count
        model.save()
        return True
    except BaseException as msg:
        print(msg)
        return False
