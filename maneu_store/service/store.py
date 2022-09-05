from maneu_store.model import Store


def store_item_all():
    return Store.objects.all().values_list('item')
