from django.forms import model_to_dict
from django.shortcuts import render

from common import verify
from maneu_users import serivce
from maneu_users.forms.InsertForm import UserInsertForm


def user_list(request):
    user_list = serivce.find_user_all()
    return render(request, 'maneu_users/user_list.html', {'user_list': user_list})


def user_detail(request):
    user_id = verify.user_id_method_get(request)
    if user_id:
        user = serivce.find_user(user_id)
        return render(request, 'maneu_users/user_detail.html', {'user': user})
    else:
        return render(request, 'maneu/error.html', {'msg': "请求出错"})


def user_delete(request):
    user_id = verify.user_id_method_get(request)
    if user_id:
        serivce.user_delete(user_id)
        return user_list(request)
    else:
        return render(request, 'maneu/error.html', {'msg': "请求出错"})


def user_insert(request):
    return render(request, 'maneu_users/user_insert.html')


def user_update(request):
    user_id = verify.user_id_method_get(request)
    if user_id:
        user = serivce.find_user(user_id)
        if user:
            form = UserInsertForm(initial=model_to_dict(user))
            return render(request, 'maneu_users/user_update.html', {'user_id': user_id, 'form': form})
        else:
            return render(request, 'maneu/error.html', {'msg': '没有订单'})
    else:
        return render(request, 'maneu/error.html', {'msg': "请求出错"})
