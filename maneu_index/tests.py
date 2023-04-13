from django.shortcuts import render

from common import common
from maneu_index import service


# Create your views here.

def index(request):
    year = common.year()
    month1 = common.month()
    month2 = request.POST.get('time')
    users_id = request.session.get('id')
    if month2 is None:
        # 判断是否有提交日期如果有就更改
        list = [0, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        month2 = list[month1]
    thisMonth = find_log(year=year, month=month1, users_id=users_id)
    otherMonth = find_log(year=year, month=month2, users_id=users_id)
    return render(request, 'maneu_index/index.html', {'guess_month_count': service.find_guess_month(users_id=users_id, month=month1, year=year).count(),
                                                      'service_month_count': service.find_service_month(users_id=users_id, month=month1, year=year).count(),
                                                      'orderv1_month_count': service.find_orderV1_month(users_id=users_id, month=month1, year=year).count(),
                                                      'orderv2_month_count': service.find_orderV2_month(users_id=users_id, month=month1, year=year).count(),
                                                      'thisMonth': thisMonth, 'otherMonth':otherMonth
                                                      })


def find_log(year='', month='', users_id=''):
    demo = {"01": 1, "02": 1, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0,
            "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0,
            "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0,
            "31": 0}
    data = {}
    guessMonthCount = service.find_orderV2_month(users_id=users_id, month=month, year=year).count()
    if guessMonthCount:
        guessLog = {}
        for i in range(1, 32):guessLog[i] = service.find_guess_day(users_id=users_id, month=month, year=year, day=i).count()
    else:
        guessLog = demo
    data['guessLog'] = guessLog
    serviceMonthCount = service.find_orderV2_month(users_id=users_id, month=month, year=year)
    if serviceMonthCount:
        serviceLog = {}
        for i in range(1, 32):serviceLog[i] = service.find_service_day(users_id=users_id, month=month, year=year, day=i).count()
    else:
        serviceLog = demo
    data['serviceLog'] = serviceLog
    orderV1MonthCount = service.find_orderV1_month(users_id=users_id, month=month, year=year)
    if orderV1MonthCount:
        orderV1Log = {}
        for i in range(1, 32):orderV1Log[i] = service.find_orderV1_day(users_id=users_id, month=month, year=year, day=i).count()
    else:
        orderV1Log = demo
    data['orderV1Log'] = orderV1Log
    orderV2MonthCount = service.find_orderV2_month(users_id=users_id, month=month, year=year)
    if orderV2MonthCount:
        orderV2Log = {}
        for i in range(1, 32):orderV2Log[i] = service.find_orderV2_day(users_id=users_id, month=month, year=year, day=i).count()
    else:
        orderV2Log = demo
    data['orderV2Log'] = orderV1Log
    return data