from maneu_store.models import ManeuStore


def store_item_all():
    return ManeuStore.objects.all()
