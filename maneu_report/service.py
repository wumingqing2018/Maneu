import json

from django.db.models import Q

from maneu.models import *


def report_index(admin_id='', start='', end=''):
    return ManeuReport.objects.filter(admin_id=admin_id, time__gte=start, time__lte=end).order_by('-time').all()


def report_search(admin_id='', text=''):
    return ManeuReport.objects.filter(Q(name__icontains=text, admin_id=admin_id) | Q(phone__icontains=text, admin_id=admin_id)).all()


def report_delete(admin_id='', id=''):
    return ManeuReport.objects.filter(admin_id=admin_id, id=id).all().delete()


def report_insert(admin_id='', guest_id='', time=''):
    return ManeuReport.objects.create(admin_id=admin_id, guess_id=guest_id, time=time, content=content)
