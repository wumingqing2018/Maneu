import json

from django.shortcuts import render

from common import common
from maneu_index import service


# Create your views here.

def index(request):
    year = common.year()
    month = common.month()
    content = {'thisMonth_guess': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                   0, 0, 0],
               'otherMonth_guess': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    0, 0, 0],
               'thisMonth_service': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0],
               'otherMonth_service': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, 0],
               'thisMonth_orderv1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0],
               'otherMonth_orderv1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, 0],
               'thisMonth_orderv2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0],
               'otherMonth_orderv2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, 0],
               }
    admin_id = request.session.get('id')
    content['guess_count'] = service.find_guess_month(admin_id=admin_id, month=month, year=year).count()
    content['orderv1_count'] = service.find_orderV1_month(admin_id=admin_id, month=month, year=year).count()
    content['orderv2_count'] = service.find_orderV2_month(admin_id=admin_id, month=month, year=year).count()
    content['service_count'] = service.find_service_month(admin_id=admin_id, month=month, year=year).count()

    if content['guess_count'] != 0:
        for i in range(1, 32):
            content['thisMonth_guess'][i-1] = service.find_guess_day(admin_id=admin_id, day=i, month=month, year=year).count()
            content['otherMonth_guess'][i-1] = service.find_guess_day(admin_id=admin_id, day=i, month=month-1, year=year).count()

    if content['orderv1_count'] != 0:
        for i in range(1, 32):
            content['thisMonth_orderv1'][i-1] = service.find_orderV1_day(admin_id=admin_id, day=i, month=month, year=year).count()
            content['otherMonth_orderv1'][i-1] = service.find_orderV1_day(admin_id=admin_id, day=i, month=month-1, year=year).count()

    if content['orderv2_count'] != 0:
        for i in range(1, 32):
            content['thisMonth_orderv2'][i-1] = service.find_orderV2_day(admin_id=admin_id, day=i, month=month, year=year).count()
            content['otherMonth_orderv2'][i-1] = service.find_orderV2_day(admin_id=admin_id, day=i, month=month-1, year=year).count()


    if content['service_count'] != 0:
        for i in range(1, 32):
            content['thisMonth_service'][i-1] = service.find_service_day(admin_id=admin_id, day=i, month=month, year=year).count()
            content['otherMonth_service'][i-1] = service.find_service_day(admin_id=admin_id, day=i, month=month-1, year=year).count()
    print(content)
    return render(request, 'maneu_index/index.html', content)
