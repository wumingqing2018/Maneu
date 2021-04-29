from django.http import JsonResponse
from user import serivce


def user_login(request):
    """登录接口"""
    if request.method == 'POST':
        from .forms.loginForm import LoginForm
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = 'admin'
            res = {'code': 0, 'msg': '登录成功'}
        else:
            res = {'code': 2, 'msg': form.errors}
    else:
        res = {'code': 1, 'msg': '请求错误'}
    return JsonResponse(res)


def user_list(request):
    if request.method == 'GET':
        user_list = serivce.find_all_user().values_list('user_id', 'nickname', 'status', 'level')
        res = {'code': 0, 'msg': 'succeed', 'data': list(user_list)}
    else:
        res = {'code': 1, 'msg': 'failed', 'data': []}
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
