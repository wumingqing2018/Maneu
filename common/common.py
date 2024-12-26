import datetime
import json
import os
import random
import time

from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.client import AcsClient
from aliyunsdkdysmsapi.request.v20170525.SendSmsRequest import SendSmsRequest


def current_time():
    """
    返回当前时间
    格式: Y-M-D H:M:S
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def yesterday(days):
    now = datetime.date.today()
    timedelta = datetime.timedelta(days=days)
    return now - timedelta


def res():
    """
    约束返回json格式
    code: 状态代码
    date: 信息内容
    msg: 返回信息
    """
    return {'status': False, 'code': '', 'msg': '', 'data': {}}


def getip(request):
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        return request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        return request.META.get("REMOTE_ADDR")


def subjective_content(request):
    content = {'OD_VA': request.POST['OD_VA'], 'OD_SPH': request.POST['OD_SPH'], 'OD_CYL': request.POST['OD_CYL'],
               'OD_AX': request.POST['OD_AX'], 'OD_ADD': request.POST['OD_ADD'], 'OD_BCVA': request.POST['OD_BCVA'],
               'OD_AL': request.POST['OD_AL'], 'OD_AK': request.POST['OD_AK'], 'OD_AD': request.POST['OD_AD'],
               'OD_CCT': request.POST['OD_CCT'], 'OD_LT': request.POST['OD_LT'], 'OD_VT': request.POST['OD_VT'],
               'OS_VA': request.POST['OS_VA'], 'OS_SPH': request.POST['OS_SPH'], 'OS_CYL': request.POST['OS_CYL'],
               'OS_AX': request.POST['OS_AX'], 'OS_ADD': request.POST['OS_ADD'], 'OS_BCVA': request.POST['OS_BCVA'],
               'OS_AL': request.POST['OS_AL'], 'OS_AK': request.POST['OS_AK'], 'OS_AD': request.POST['OS_AD'],
               'OS_CCT': request.POST['OS_CCT'], 'OS_LT': request.POST['OS_LT'], 'OS_VT': request.POST['OS_VT'],
               'remark': request.POST['remark']}
    return content


def getEveryDay(begin_date, end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


def sendsms(code, call):
    credentials = AccessKeyCredential(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
                                      os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])

    request = SendSmsRequest()
    request.set_accept_format('json')
    request.set_SignName("徕可")
    request.set_TemplateCode("SMS_471990239")
    request.set_PhoneNumbers(call)
    request.set_TemplateParam({'code': code})

    client = AcsClient(region_id='cn-shenzhen', credential=credentials)
    response = client.do_action_with_exception(request)

    return eval(response)


def get_random_code():
    return random.randint(100000, 999999)


def guest_simple(request):
    simple = {'remark': '', 'time': current_time(), 'name': '', 'call': '', 'age': '', 'sex': '', 'dfh': '无',
              'ot': '正', 'em': '左'}

    for i in list(simple):
        try:
            if request.GET.get(i):
                simple[i] = request.GET.get(i)
        except:
            pass

    return simple


def report_simple(request_dict):
    request = json.loads(request_dict)
    data = {
        'Function': '远用解决方案',
        'PD': '',
        'OD': {
            'AL': '', 'AK': '', 'AX': '0.00', 'AD': '', 'ADD': '0.00', 'BC': '', 'CYL': '0.00', 'CCT': '', 'VA': '', 'SPH': '0.00',
            'PR': '0.00', 'FR': '', 'LT': '', 'VT': ''
        },
        'OS': {
            'AL': '', 'AK': '', 'AX': '0.00', 'AD': '', 'ADD': '0.00', 'BC': '', 'CYL': '0.00', 'CCT': '', 'VA': '', 'SPH': '0.00',
            'PR': '0.00', 'FR': '', 'LT': '', 'VT': ''
        }
    }



    try:
        if request['Function'] == '两用解决方案' or '远用解决方案' or '近用解决方案':
            data['Function'] = request['Function']
    except Exception as e:
        print(e)

    try:
        data['PD'] = int(request['PD'])
    except:
            pass

    for i in list(data['OD']):
        try:
            data['OD'][i] = format(float(request['OD'][i]), '.2f')
        except:
            pass

    for i in list(data['OS']):
        try:
            data['OS'][i] = format(float(request['OS'][i]), '.2f')
        except:
            pass
    return json.dumps(data)
