from django.shortcuts import HttpResponse
from django.shortcuts import render

from common import verify
from user import serivce
from user import server_redis
from user.forms.loginForm import LoginForm


def user_logout(request):
    session_key = request.session.session_key
    server_redis.del_user_login(session_key)
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
