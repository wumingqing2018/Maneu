from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from user import serivce
from common import verify


def user_login(request):
    """
    登录模块
    判断用户是否登录
    """
    from .forms.loginForm import LoginForm
    try:
        user = request.session['user']
    except Exception as msg:
        user = ''
        print(msg)
    if user:
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
            return render(request, 'user/user_login.html', {'form': LoginForm()})


def user_logout(request):
    from .forms.loginForm import LoginForm
    request.session['user'] = None
    return render(request, 'user/user_login.html', {'form': LoginForm()})


def user_list(request):
    return render(request, 'user/user_list.html', {'user_list': serivce.find_all_user()})


def user_detail(request):
    user_id = verify.user_id_method_get(request)
    if user_id:
        user = serivce.find_user(user_id)
        return render(request, 'user/user_detail.html', {'user': user})
    else:
        return HttpResponse('请求出错')


def user_insert(request):
    return render(request, 'user/user_insert.html', )


def user_update(request):
    user_id = verify.user_id_method_get(request)
    if user_id:
        user = serivce.find_user(user_id)
        return render(request, 'user/user_update.html', {'user': user})
    else:
        return HttpResponse('请求出错')
