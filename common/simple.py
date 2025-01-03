import json
from common.common import current_time


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

def order_simple(request_dict):
    request = json.loads(request_dict)
    simple = {'arg10':'', 'arg11':'', 'arg12':'', 'arg13':'', 'arg14':''}
    data = []
    for i in request:
        if i != simple:
            data.append(i)

    return json.dumps(data)


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
    except:
        pass

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
