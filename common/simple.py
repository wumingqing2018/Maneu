import json
from common.common import current_time


def guest_simple(request):
    simple = {'remark': '', 'time': current_time(), 'name': '', 'call': '', 'age': '', 'sex': '', 'dfh': '无',
              'ot': '正', 'em': '左'}

    for i in list(simple):
        try:
            if request.GET.get(i): simple[i] = request.GET.get(i)
        except:
            pass

    return simple

def order_simple(request_dict):
    simple = {'arg10':'', 'arg11':'', 'arg12':'', 'arg13':'', 'arg14':''}
    data = []

    try:
        request = json.loads(request_dict)
        for i in request:
            if i != simple: data.append(i)
    except:
        pass

    if len(data)==0: data.append({'arg10':'无', 'arg11':'无', 'arg12':'无', 'arg13':'无', 'arg14':'无'})

    return json.dumps(data)


def report_simple(request_dict):
    request = json.loads(request_dict)
    data = {
        'PLAN': '远用解决方案',
        'PD': '',
        'OD': {
            'AL': '', 'AK': '', 'AX': '0.00', 'AD': '', 'ADD': '0.00', 'BC': '', 'CYL': '0.00', 'CCT': '', 'VA': '', 'SPH': '0.00', 'PR': '0.00', 'FR': '', 'LT': '', 'VT': ''
        },
        'OS': {
            'AL': '', 'AK': '', 'AX': '0.00', 'AD': '', 'ADD': '0.00', 'BC': '', 'CYL': '0.00', 'CCT': '', 'VA': '', 'SPH': '0.00', 'PR': '0.00', 'FR': '', 'LT': '', 'VT': ''
        }
    }

    try:
        if request['PLAN'] == '两用解决方案' or '远用解决方案' or '近用解决方案': data['PLAN'] = request['PLAN']
    except:
        pass

    try:
        data['PD'] = format(float(request['PD']), '.1f')
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

    try:
        if request['OD']['FR'] == 'BU' or 'BD' or 'BO' or 'BI': data['OD']['FR'] = request['OD']['FR']
    except:
        pass

    try:
        if request['OS']['FR'] == 'BU' or 'BD' or 'BO' or 'BI': data['OS']['FR'] = request['OS']['FR']
    except:
        pass

    return json.dumps(data)
