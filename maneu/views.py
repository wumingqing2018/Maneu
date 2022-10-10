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
    print(service.ManeuDatalogs_List(user_id=user_id))
    dataLogs = json.loads(service.ManeuDatalogs_List(user_id=user_id).order_log)
    for i in dataLogs['order_log']:
        order_log.append(dataLogs['order_log'][i])
        dataLogs['order_count'] = dataLogs['order_count'] + dataLogs['order_log'][i]
        money_log.append(dataLogs['money_log'][i])
        dataLogs['money_count'] = dataLogs['money_count'] + dataLogs['money_log'][i]
    return render(request, 'maneu/test1.html', {'order_log': order_log, 'money_log': money_log, 'money_count': dataLogs['money_count'], 'order_count': dataLogs['order_count']})


def test2(request):
    test = []
    for i in range(1,10):
        test.append(random.randint(0,10))
    print(test)
    return render(request, 'maneu/test1.html', )
