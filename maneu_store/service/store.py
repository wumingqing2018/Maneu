from common import common
from maneu_store.models import Store


def store_item_all():
    return Store.objects.all().values_list('item')
