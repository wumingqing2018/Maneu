
from os import name
from maneu_class.models import ManeuClass


def class_list():
    return ManeuClass.objects.all()

