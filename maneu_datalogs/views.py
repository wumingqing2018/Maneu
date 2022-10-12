from django.shortcuts import render
from common import common
from maneu_datalogs import service
import json, datetime
# Create your views here.

def index(request):
    if request.method == 'POST':
        now_month = request.POST.get('time')[5:7]
        print(now_month)
    else:
        now_month = common.month()
    user_id = request.session.get('id')
    order_log = []
    money_log = []
    class_log = []
    store_list = ['arg14', 'arg24', 'arg34', 'arg44', 'arg54']
    class_list = ['arg11', 'arg21', 'arg31', 'arg41', 'arg51']

    order_logs = {
        "order_log": {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0,
                      "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0,
                      "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0,
                      "31": 0},
        "order_count": 0,
        "money_log": {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0,
                      "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0,
                      "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0,
                      "31": 0},
        "money_count": 0,
        "class_log": {},
        "class_count": 0,
    }
    orderlist = service.find_order_month(users_id=user_id, month=now_month)  # 查找今日订单
    for order in orderlist:
        order_logs['order_count'] = order_logs['order_count'] + 1
        order_logs['order_log']['%02d'%order.time.day] = order_logs['order_log']['%02d'%order.time.day] +1
        store = json.loads(service.find_store_id(id=order.store_id).content)
        for i in store_list:
            try:
                store[i] = int(store[i])
            except:
                store[i] = 0
            order_logs['money_count'] = order_logs['money_count'] + store[i]
            order_logs['money_log']['%02d' % order.time.day] = order_logs['money_log']['%02d'%order.time.day] + store[i]
        for i in class_list:

            if store[i]:
                if order_logs['class_log'].get(store[i]):
                    order_logs['class_log'][store[i]] = order_logs['class_log'][store[i]] +1
                else:
                    order_logs['class_log'][store[i]] = 1
    for i in order_logs['order_log']:
        order_log.append(order_logs['order_log'][i])
        money_log.append(order_logs['money_log'][i])

    for i in order_logs['class_log']:
        class_log.append({'value': order_logs['class_log'][i], 'name': i})
    return render(request, 'maneu_datalogs/index.html', {'order_log': order_log, 'order_count': order_logs['order_count'],
                                                         'money_log': money_log, 'money_count': order_logs['money_count'],
                                                         'class_log': class_log, 'class_count': order_logs['class_count'],
                                                         })
