from django.shortcuts import render

from common import common
from maneu_index import service


# Create your views here.

def index(request):
    return render(request, 'maneu_index/index.html')
