from django.shortcuts import render

from common import verify
from maneu_users import serivce


def user_list(request):
    return render(request, 'user/user_list.html', {'user_list': serivce.find_user_all()})


def user_detail(request):
    user_id = verify.user_id_method_get(request)
    if user_id:
        user = serivce.find_user(user_id)
        return render(request, 'user/user_detail.html', {'maneu_users': user})
    else:
        return render(request, 'maneu/error.html', {'msg': "请求出错"})


def user_insert(request):
    return render(request, 'user/user_insert.html')


def user_update(request):
    user_id = verify.user_id_method_get(request)
    if user_id:
        user = serivce.find_user(user_id)
        return render(request, 'user/user_update.html', {'maneu_users': user})
    else:
        return render(request, 'maneu/error.html', {'msg': "请求出错"})
