import json

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
        else:
            print(form.errors)
    print(request.session.flush())  # 删除服务端的session，删除当前的会话数据并删除会话的Cookie。
    print(request.session.get('id'))
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
                print(msg)
                return render(request, 'maneu/guess.html', {'msg': '没有您的订单'})

    return render(request, 'maneu/guess.html')


def test1(request):
    user_id = request.session.get('id')
    dataLogs = service.ManeuDatalogs_List(user_id=user_id, time=common.month())
    if dataLogs == None:
        orderCountList = {}
        ten = []
        for i in range(1, 32):
            ten.append(service.ManeuOrder_count(time='2022-10-'+'%02d'%i, user_id=user_id))
        nine = []
        for i in range(1, 31):
            nine.append(service.ManeuOrder_count(time='2022-09-'+'%02d'%i, user_id=user_id))
        orderCountList['cur_month'] = ten
        orderCountList['yest_month'] = nine

        service.ManeuDatalogs_getorcreate(user_id=user_id, time=common.today(), order_log=json.dumps(orderCountList))
        dataLogs = service.ManeuDatalogs_List(user_id=user_id, time=common.month())
    return render(request, 'maneu/test1.html', {'dataLogs': json.loads(dataLogs.order_log)})


def test2(request):
    user_id = request.session.get('id')
    orderCountList = {"yest_month": [15, 6, 1, 7, 8, 1, 7, 3, 6, 3, 10, 14, 15, 5, 4, 3, 5, 6, 3, 12, 5, 2, 2, 4, 3, 5, 6, 3, 4, 2, 4], "cur_month": [4, 6, 5, 3, 4, 5, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    service.ManeuDatalogs_getorcreate(user_id=user_id, time=common.today(), order_log=json.dumps(orderCountList))
    return HttpResponseRedirect(reverse('test1'))