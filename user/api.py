from .forms.loginForm import LoginForm
from django.http import JsonResponse


def login(request):
    """登录接口"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = 'admin'
            res = {'code': 0, 'msg': '登录成功'}
        else:
            res = {'code': 2, 'msg': form.errors}
    else:
        res = {'code': 1, 'msg': '请求错误'}
    return JsonResponse(res)


def user_insert(request):
    from user.forms.userInsertForm import UserInsertForm
    if request.method == 'POST':
        form = UserInsertForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            res = {'code': 0, 'data': data}
        else:
            res = {'code': 2, 'data': form.errors}
    else:
        res = {'code': 1, 'data': 'post'}
    return JsonResponse(res)



def user_freeze(request):
    res = {'code': 1, 'msg': '请求错误'}
    return JsonResponse(res)


def user_unfreeze(request):
    res = {'code': 1, 'msg': '请求错误'}
    return JsonResponse(res)
