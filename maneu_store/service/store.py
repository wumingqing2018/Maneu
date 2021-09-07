from common import common
from store.models import Store


def store_item_all():
    return Store.objects.all().values_list('item')
