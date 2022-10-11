import json
import random

from django.shortcuts import HttpResponseRedirect, reverse, render

from common import common
from maneu import service
from maneu.forms.guessForm import GuessForm
from maneu.forms.loginForm import LoginForm


def index(request):
    """
    首页
    """
    return render(request, 'maneu/index.html')


def login(request):
    """
    登录模块
    获取session key并根据sessionkey 判断用户是否已经登录
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_content = service.find_user_username(username=request.POST['username'])
            request.session['ip'] = common.get_ip(request)
            request.session['id'] = user_content.user_id
            request.session['nickname'] = user_content.nickname
            return HttpResponseRedirect(reverse('maneu_order:order_list'))
    return render(request, 'maneu/login.html', {'form': LoginForm()})


def guess(request):
    if request.method == 'POST':
        form = GuessForm(request.POST)
        if form.is_valid():
            try:
                order = service.find_order_phone(phone=request.POST['phone'])[0]
                users = service.find_users_id(id=order.users_id)
                guess = service.find_guess_id(id=order.guess_id)
                store = service.find_store_id(id=order.store_id)
                visionsolutions = service.find_ManeuVisionSolutions_id(id=order.visionsolutions_id)
                subjectiverefraction = service.find_subjectiverefraction_id(id=order.subjectiverefraction_id)
                return render(request, 'maneu/detail.html',
                              {'order': order, 'users': users, 'guess': guess, 'store': json.loads(store.content),
                               'visionsolutions': json.loads(visionsolutions.content),
                               'subjectiverefraction': json.loads(subjectiverefraction.content)})
            except BaseException as msg:
                return render(request, 'maneu/guess.html', {'msg': '没有您的订单'})

    return render(request, 'maneu/guess.html')


def test1(request):
    user_id = request.session.get('id')
    order_log = []
    money_log = []
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
        }
    orderlist = service.find_order_all(users_id=user_id)  # 查找今日订单
    for order in orderlist:
        time = order.time
        month = time.strftime("%m")
        day = time.strftime("%d")
        store_count = 0
        Datalogs = service.Datalogs_time(users_id=user_id, time=month)
    return render(request, 'maneu/test1.html',)
