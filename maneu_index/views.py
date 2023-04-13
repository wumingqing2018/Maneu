from django.shortcuts import render

from common import common
from maneu_index import service


# Create your views here.

def index(request):
    year = common.year()
    month1 = common.month()
    month2 = request.POST.get('time')
    admin_id = request.session.get('id')

    if month2 is None:
        # 判断是否有提交日期如果有就更改
        list = [0, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        month2 = list[month1]
    thisMonth = find_log(year=year, month=month1, admin_id=admin_id)
    otherMonth = find_log(year=year, month=month2, admin_id=admin_id)
    return render(request, 'maneu_index/index.html', {'guess_month_count': service.find_guess_month(admin_id=admin_id, month=month1, year=year).count(),
                                                      'service_month_count': service.find_service_month(admin_id=admin_id, month=month1, year=year).count(),
                                                      'orderv1_month_count': service.find_orderV1_month(admin_id=admin_id, month=month1, year=year).count(),
                                                      'orderv2_month_count': service.find_orderV2_month(admin_id=admin_id, month=month1, year=year).count(),
                                                      'thisMonth': thisMonth, 'otherMonth': otherMonth,
                                                      })


def find_log(year='', month='', admin_id=''):
    data = {'guessLog': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'serviceLog': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'orderV1Log': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'orderV2Log': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            }
    guessMonthCount = service.find_orderV2_month(admin_id=admin_id, month=month, year=year)
    if guessMonthCount:
        for i in range(1, 32):
            data['guessLog'].append(service.find_guess_day(admin_id=admin_id, month=month, year=year, day=i).count())
    serviceMonthCount = service.find_orderV2_month(admin_id=admin_id, month=month, year=year)
    if serviceMonthCount:
        for i in range(1, 32):
            data['serviceLog'].append(service.find_service_day(admin_id=admin_id, month=month, year=year, day=i).count())
    orderV1MonthCount = service.find_orderV1_month(admin_id=admin_id, month=month, year=year)
    if orderV1MonthCount:
        for i in range(1, 32):
            data['orderV1Log'].append(service.find_orderV1_day(admin_id=admin_id, month=month, year=year, day=i).count())
    orderV2MonthCount = service.find_orderV2_month(admin_id=admin_id, month=month, year=year)
    if orderV2MonthCount:
        for i in range(1, 32):
            data['orderV2Log'].append(service.find_orderV2_day(admin_id=admin_id, month=month, year=year, day=i).count())
    return data