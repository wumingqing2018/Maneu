import os, re, random

from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.client import AcsClient
from aliyunsdkdysmsapi.request.v20170525.SendSmsRequest import SendSmsRequest
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, reverse, render

from common import common
from maneu import service
from common.forms.loginForm import LoginForm


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
            return HttpResponseRedirect(reverse('maneu_index:index'))
        else:
            print(form.errors)
    return render(request, 'maneu/login.html', {'form': LoginForm()})


def verify(request):
    return JsonResponse()


def sendsms(request):
    pattern = re.compile(r'^1[3-9]\d{9}$')
    phone_number = request.GET.get('call')
    if pattern.match(phone_number) is not None:
        random_num = random.randint(111111, 999999)
        data = service.sendsms(phone=phone_number, password=random_num)
        if data is not None:
            # Please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set.
            credentials = AccessKeyCredential(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
                                              os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])
            # use STS Token
            # credentials = StsTokenCredential(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'], os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'], os.environ['ALIBABA_CLOUD_SECURITY_TOKEN'])
            client = AcsClient(region_id='cn-shenzhen', credential=credentials)

            request = SendSmsRequest()
            request.set_accept_format('json')
            request.set_SignName("徕可")
            request.set_TemplateCode("SMS_471990239")
            request.set_PhoneNumbers(phone_number)
            request.set_TemplateParam({'code': random_num})

            response = client.do_action_with_exception(request)
            response = eval(response)

            if response['Code'] == 'OK':
                content = {'status': True, 'message': 'OK', 'data': {}}
            else:
                content = {'status': False, 'message': '', 'data': response}
        else:
            content = {'status': False, 'message': 'phone is :none', 'data': {}}
    else:
        content = {'status': False, 'message': 'code is :none', 'data': {}}

    return JsonResponse(content)