from os import pread

from django.http import JsonResponse
from django.shortcuts import render

from common import common
from common.verify import *
from maneu import service


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
    return render(request, 'maneu/login.html')


def login_api(request):
    call = is_call(request.GET.get('call'))
    code = is_code(request.GET.get('code'))

    if code and call:
        admin = service.admin_login(call, code)
        if admin:
            request.session['ip'] = common.getip(request)
            request.session['id'] = admin.id
            request.session['nickname'] = admin.nickname
            content = {'status': True, 'message': '', 'data': {}}
        else:
            content = {'status': False, 'message': '请确认手机号', 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的手机号和验证码', 'data': {}}

    return JsonResponse(content)


def sendsms(request):
    phone_number = is_call(request.GET.get('call'))

    if phone_number:
        random_num = common.get_random_code()
        data = service.sendsms(call=phone_number, code=random_num)
        if data:
            response = common.sendsms(call=phone_number, code=random_num)
            if response['Code'] == 'OK':
                content = {'status': True, 'message': 'OK', 'data': {}}
            else:
                content = {'status': False, 'message': response["Message"], 'data': {}}
        else:
            content = {'status': False, 'message': 'phone is :none', 'data': {}}
    else:
        content = {'status': False, 'message': 'code is :none', 'data': {}}
    print(content)
    return JsonResponse(content)
