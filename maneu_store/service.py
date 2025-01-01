from maneu.models import ManeuStore
from django.db.models import Q


def store_index(admin_id='', start='', end=''):
    return ManeuStore.objects.filter(admin_id=admin_id, time__gte=start, time__lte=end).order_by('-time').all()


def store_id(id=''):
    return ManeuStore.objects.filter(id=id).first()


def store_insert(admin_id='', guest_id='', time='', content=''):
    return ManeuStore.objects.create(admin_id=admin_id, guess_id=guest_id, time=time, content=content)


def store_delete(id=''):
    return ManeuStore.objects.filter(id=id).all().delete()


def store_update(id='', content=''):
    return ManeuStore.objects.filter(id=id).update(content=content)


def store_search(admin_id='', text=''):
    return ManeuStore.objects.filter(Q(name__icontains=text, admin_id=admin_id) | Q(phone__icontains=text, admin_id=admin_id)).all()
