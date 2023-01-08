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
            request.session['id'] = user_content.id
            request.session['nickname'] = user_content.nickname
            return HttpResponseRedirect(reverse('maneu_order:order_list'))
    return render(request, 'maneu/admin.html', {'form': LoginForm()})


def guess(request):
    if request.method == 'POST':
        form = GuessForm(request.POST)
        if form.is_valid():
                guess = service.find_guess_phone(phone=request.POST.get('phone'))
                if guess != None:
                    request.session['id'] = guess.id
                    return HttpResponseRedirect(reverse('guess_admin:order_list'))
                return render(request, 'maneu/guess.html', {'msg': '没有您的订单'})

    return render(request, 'maneu/guess.html')
