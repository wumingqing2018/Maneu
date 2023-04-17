import json

from django.shortcuts import render

from common import common
from maneu_index import service


# Create your views here.

def index(request):
    year = common.year()
    month = common.month()
    content = {}
    admin_id = request.session.get('id')
    demo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    content['guess_count'] = service.find_guess_month(admin_id=admin_id, month=month, year=year).count()
    content['orderv1_count'] = service.find_orderV1_month(admin_id=admin_id, month=month, year=year).count()
    content['orderv2_count'] = service.find_orderV2_month(admin_id=admin_id, month=month, year=year).count()
    content['service_count'] = service.find_service_month(admin_id=admin_id, month=month, year=year).count()

    if content['guess_count'] == 0:
        content['thisMonth_guess'] = demo
        content['otherMonth_guess'] = demo
    else:
        content['thisMonth_guess'] = []
        content['otherMonth_guess'] = []
        for i in range(1, 32):
            content['thisMonth_guess'].append(service.find_guess_day(admin_id=admin_id, day=i, month=month, year=year).count())
            content['otherMonth_guess'].append(service.find_guess_day(admin_id=admin_id, day=i, month=month-1, year=year).count())

    if content['orderv1_count'] == 0:
        content['thisMonth_orderv1'] = demo
        content['otherMonth_orderv1'] = demo
    else:
        content['thisMonth_orderv1'] = []
        content['otherMonth_orderv1'] = []
        for i in range(1, 32):
            content['thisMonth_orderv1'].append(service.find_orderV1_day(admin_id=admin_id, day=i, month=month, year=year).count())
            content['otherMonth_orderv1'].append(service.find_orderV1_day(admin_id=admin_id, day=i, month=month-1, year=year).count())

    if content['orderv2_count'] == 0:
        content['thisMonth_orderv2'] = demo
        content['otherMonth_orderv2'] = demo
    else:
        content['thisMonth_orderv2'] = []
        content['otherMonth_orderv2'] = []
        for i in range(1, 32):
            content['thisMonth_orderv2'].append(service.find_orderV2_day(admin_id=admin_id, day=i, month=month, year=year).count())
            content['otherMonth_orderv2'].append(service.find_orderV2_day(admin_id=admin_id, day=i, month=month-1, year=year).count())


    if content['service_count'] == 0:
        content['thisMonth_service'] = demo
        content['otherMonth_service'] = demo
    else:
        content['thisMonth_service'] = []
        content['otherMonth_service'] = []
        for i in range(1, 32):
            content['thisMonth_service'].append(service.find_service_day(admin_id=admin_id, day=i, month=month, year=year).count())
            content['otherMonth_service'].append(service.find_service_day(admin_id=admin_id, day=i, month=month-1, year=year).count())
    print(content)
    return render(request, 'maneu_index/index.html', content)
