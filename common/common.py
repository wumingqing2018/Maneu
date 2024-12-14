import datetime
import json
import os
import random
import time
from logging import exception

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


def guest_simple(reuqest_dict):
    reuqest_dict = reuqest_dict.dict()
    simple = {'remark': '', 'time': current_time(), 'name': '', 'call': '', 'age': '0', 'sex': '男', 'DFH': '无',
              'OT': '正', 'EM': '左'}

    simple.update(reuqest_dict)
    return simple


def report_simple(reuqest_dict):
    reuqest = json.loads(reuqest_dict)

    try:
        if reuqest['Function'] == '两用解决方案':
            reuqest['PLAN'] = reuqest['Function']
        elif reuqest['Function'] == '近用解决方案':
            reuqest['PLAN'] = reuqest['Function']
        elif reuqest['Function'] == '远用解决方案':
            reuqest['PLAN'] = reuqest['Function']
        else:
            reuqest['PLAN'] = '两用解决方案'
            del reuqest['Function']
    except:
        reuqest['PLAN'] = '两用解决方案'

    try:
        reuqest['PD'] = float(reuqest['PD'])
    except:
        reuqest['PD'] = 60

    data = {'VA': 1.0,
            'SPH': 0,
            'CYL': 0,
            'AX': 90,
            'PR': 10,
            'FR': 0,
            'ADD': 1.0,
            'AL': 24,
            'AK': 39,
            'AD': 2.5,
            'CCT': 0.5,
            'LT': 3.5,
            'VT': 16,
            'BCVA': 1.0,
            }

    for i in list(data.keys()):
        try:
            float(reuqest['OD'][i])
        except:
            reuqest['OD'][i] = data[i]

    for i in list(data.keys()):
        try:
            float(reuqest['OS'][i])
        except :
            reuqest['OS'][i] = data[i]
    return json.dumps(reuqest)
