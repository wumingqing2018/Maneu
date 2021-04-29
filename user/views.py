from django.shortcuts import render
from django.shortcuts import redirect
from .forms.loginForm import LoginForm
from .serivce import *


def user_login(request):
    """
    登录模块
    判断用户是否登录

    """
    if request.session['user']:
        return redirect('index_page')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                request.session['user'] = 'admin'
                return redirect('index_page')
            else:
                return render(request, 'user/user_login.html', {'form': LoginForm()})
        else:
            request.session['user'] = None
            print('test')
            return render(request, 'user/user_login.html', {'form': LoginForm()})


def user_logout(request):
    request.session['user'] = None
    form = LoginForm()
    return render(request, 'user/user_login.html', {'form': form})


def user_list(request):
    user_list = find_all_user
    return render(request, 'user/user_list.html', {'user_list': user_list})


def user_content(request):
    if request.method == 'GET':
        id = request.GET['user_id']
        user = find_user(user_id=id)
    return render(request, 'user/user_page.html', {'user': user})


def user_insert(request):
    return render(request, 'user/user_insert.html', )


def user_update(request):
    return render(request, 'user/user_update.html')
