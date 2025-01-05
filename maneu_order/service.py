from django.db.models import Q
import json
from maneu.models import ManeuOrder, ManeuReport, ManeuStore
from common.simple import order_simple

def test():
    orderList =  ManeuOrder.objects.filter().all()
    for order in orderList:
        store = ManeuStore.objects.filter(id=order.store_id).first()
        try:
            content = json.loads(store.content)
            try:
                del content['time']
            except:
                pass
            try:
                if content['remark'] != order.remark:
                    remark = content['remark'] + ',' + order.remark
                else:
                    remark = ''
            except:
                remark = ''
            key = list(content)[0]
            if type(content[key]) == list:
                data = []
                for i in list(content):
                    simple = {'arg10': '', 'arg11': '', 'arg12': '', 'arg13': '', 'arg14': ''}
                    simple['arg10'] = content[i][0]
                    simple['arg11'] = content[i][1]
                    simple['arg12'] = content[i][2]
                    simple['arg13'] = content[i][3]
                    simple['arg14'] = content[i][4]
                    data.append(simple)
                data = json.dumps(data)
                ManeuOrder.objects.filter(id=order.id).update(content=order_simple(data) ,remark=remark)
            else:
                data = [
                    {"arg10": content['arg10'], "arg11": content['arg11'], "arg12": content['arg12'], "arg13": content['arg13'], "arg14": content['arg14']},
                    {"arg10": content['arg20'], "arg11": content['arg21'], "arg12": content['arg22'],
                     "arg13": content['arg23'], "arg14": content['arg24']},
                    {"arg10": content['arg30'], "arg11": content['arg31'], "arg12": content['arg32'],
                     "arg13": content['arg33'], "arg14": content['arg34']},
                    {"arg10": content['arg40'], "arg11": content['arg41'], "arg12": content['arg42'],
                     "arg13": content['arg43'], "arg14": content['arg44']},
                    {"arg10": content['arg50'], "arg11": content['arg51'], "arg12": content['arg52'],
                     "arg13": content['arg53'], "arg14": content['arg54']},
                ]
                data = json.dumps(data)
                ManeuOrder.objects.filter(id=order.id).update(content=order_simple(data) ,remark=remark)
        except Exception as e:
            pass


def report_delete(admin_id='', report_id=''):
    return ManeuReport.objects.filter(admin_id=admin_id, id=report_id).delete()


def order_index(admin_id='', star='', end=''):
    """
    全部订单
    """
    return ManeuOrder.objects.filter(admin_id=admin_id, time__gte=star, time__lte=end).order_by('-time').all()


def order_id(admin_id='', order_id=''):
    """
    查找指定订单
    根据时间排序
    """
    return ManeuOrder.objects.filter(id=order_id, admin_id=admin_id).first()


def order_delete(admin_id='', order_id=''):
    """
    查找指定订单a
    根据时间排序
    """
    return ManeuOrder.objects.filter(admin_id=admin_id, id=order_id).delete()


def order_search(admin_id='', text=''):
    return ManeuOrder.objects.filter(Q(name__icontains=text, admin_id=admin_id) | Q(phone__icontains=text, admin_id=admin_id)).all()


def order_insert(admin_id='', name='', time='', call='', content='', guest_id='', store_id='', report_id='', remark=''):
    return ManeuOrder.objects.create(name=name, time=time, phone=call, guest_id=guest_id, admin_id=admin_id,
                                     store_id=store_id, report_id=report_id, remark=remark, content=content)


def order_update(admin_id='', order_id='', name='', call='', time="", remark="", content=''):
    return ManeuOrder.objects.filter(id=order_id, admin_id=admin_id).update(name=name, phone=call, time=time, remark=remark, content=content)
