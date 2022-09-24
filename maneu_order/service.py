import datetime
import json

from django.db.models import Q

from common import common
from maneu_order.models import ManeuGuess
from maneu_order.models import ManeuOrder
from maneu_order.models import ManeuOrderV2
from maneu_order.models import ManeuStore
from maneu_order.models import ManeuSubjectiveRefraction
from maneu_order.models import ManeuUsers
from maneu_order.models import ManeuVisionSolutions


def find_order_all(users_id=''):
    """
    全部订单
    """
    try:
        return ManeuOrderV2.objects.filter(users_id=users_id).order_by('-time').all()
    except BaseException as msg:
        print(msg)
        return None


def find_order_id(order_id='', users_id=''):
    """
    查找指定订单
    根据时间排序
    """
    try:
        return ManeuOrderV2.objects.filter(id=order_id, users_id=users_id).first()
    except BaseException as msg:
        print(msg)
        return None


def delete_order_id(users_id='', id=''):
    """
    查找指定订单
    根据时间排序
    """
    try:
        order = ManeuOrderV2.objects.filter(users_id=users_id, id=id).all()
        return order.delete()
    except BaseException as msg:
        print(msg)
        return None


def find_order_phone(phone=''):
    try:
        return ManeuOrderV2.objects.filter(phone=phone).order_by('-time').all()
    except BaseException as msg:
        print(msg)
        return None


def find_guess_id(id=''):
    try:
        return ManeuGuess.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def delete_guess_id(id=''):
    try:
        guess = ManeuGuess.objects.filter(id=id).all()
        return guess.delete()
    except BaseException as msg:
        print(msg)
        return None


def find_store_id(id=''):
    try:
        return ManeuStore.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def delete_store_id(id=''):
    try:
        store = ManeuStore.objects.filter(id=id).first()
        return store.delete()
    except BaseException as msg:
        print(msg)
        return None


def find_users_id(id=''):
    try:
        return ManeuUsers.objects.filter(user_id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_ManeuOrderV2_search(date='', text='', users_id=''):
    if date and text:
        return ManeuOrderV2.objects.filter(Q(name=text) | Q(phone=text), Q(time__gt=date),
                                           Q(users_id=users_id)).order_by('-time').all()
    elif date and text == '':
        return ManeuOrderV2.objects.filter(Q(time__gt=date), Q(users_id=users_id)).order_by('-time').all()
    elif date == '' and text:
        return ManeuOrderV2.objects.filter(users_id=users_id).filter(Q(name=text) | Q(phone=text)).order_by(
            '-time').all()
    else:
        return None


def find_ManeuOrderV2_search_v1(date='', text='', users_id=''):
    return ManeuOrderV2.objects.filter(Q(name=text) | Q(phone=text), Q(time__gt=date), Q(users_id=users_id)).order_by(
        '-time').all()


def find_ManeuOrderV2_search_v2(date='', users_id=''):
    return ManeuOrderV2.objects.filter(Q(time__gt=date), Q(users_id=users_id)).order_by('-time').all()


def find_ManeuOrderV2_search_v3(text='', users_id=''):
    return ManeuOrderV2.objects.filter(users_id=users_id).filter(Q(name=text) | Q(phone=text)).order_by('-time').all()


def find_ManeuVisionSolutions_id(id=''):
    try:
        return ManeuVisionSolutions.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def delete_ManeuVisionSolutions_id(id=''):
    try:
        VisionSolutions = ManeuVisionSolutions.objects.filter(id=id).first()
        return VisionSolutions.delete()
    except BaseException as msg:
        print(msg)
        return None


def find_subjectiverefraction_id(id=''):
    try:
        return ManeuSubjectiveRefraction.objects.filter(id=id).first()
    except BaseException as msg:
        print(msg)
        return None


def delete_subjectiverefraction_id(id=''):
    try:
        subjectiverefraction = ManeuSubjectiveRefraction.objects.filter(id=id).first()
        return subjectiverefraction.delete()
    except BaseException as msg:
        print(msg)
        return None


def ManeuVisionSolutions_insert(VS_remark='', OD_BC_DS='', OD_BC_CYL='', OD_BC_AX='', OD_BC_PR='', OD_BC_FR='',
                                OD_BC_ADD='', OD_BC_NA='', OS_BC_DS='', OS_BC_CYL='', OS_BC_AX='', OS_BC_PR='',
                                OS_BC_FR='', OS_BC_ADD='', OS_BC_NA='', pd='', function=''):
    try:
        ManeuVisionSolutions_content = {'BC_remark': VS_remark, 'pd': pd, 'function': function,
                                        'OD_BC_DS': OD_BC_DS, 'OD_BC_CYL': OD_BC_CYL, 'OD_BC_AX': OD_BC_AX,
                                        'OD_BC_PR': OD_BC_PR, 'OD_BC_FR': OD_BC_FR, 'OD_BC_ADD': OD_BC_ADD,
                                        'OD_BC_NA': OD_BC_NA,
                                        'OS_BC_DS': OS_BC_DS, 'OS_BC_CYL': OS_BC_CYL, 'OS_BC_AX': OS_BC_AX,
                                        'OS_BC_PR': OS_BC_PR, 'OS_BC_FR': OS_BC_FR, 'OS_BC_ADD': OS_BC_ADD,
                                        'OS_BC_NA': OS_BC_NA,
                                        }
        return ManeuVisionSolutions.objects.create(content=json.dumps(ManeuVisionSolutions_content))
    except BaseException as msg:
        print(msg)
        return None


def ManeuVisionSolutions_update(id='', VS_remark='', OD_BC_DS='', OD_BC_CYL='', OD_BC_AX='', OD_BC_PR='', OD_BC_FR='',
                                OD_BC_ADD='', OD_BC_NA='', OS_BC_DS='', OS_BC_CYL='', OS_BC_AX='', OS_BC_PR='',
                                OS_BC_FR='', OS_BC_ADD='', OS_BC_NA='', pd='', function=''):
    try:
        ManeuVisionSolutions_content = {'BC_remark': VS_remark, 'pd': pd, 'function': function,
                                        'OD_BC_DS': OD_BC_DS, 'OD_BC_CYL': OD_BC_CYL, 'OD_BC_AX': OD_BC_AX,
                                        'OD_BC_PR': OD_BC_PR, 'OD_BC_FR': OD_BC_FR, 'OD_BC_ADD': OD_BC_ADD,
                                        'OD_BC_NA': OD_BC_NA,
                                        'OS_BC_DS': OS_BC_DS, 'OS_BC_CYL': OS_BC_CYL, 'OS_BC_AX': OS_BC_AX,
                                        'OS_BC_PR': OS_BC_PR, 'OS_BC_FR': OS_BC_FR, 'OS_BC_ADD': OS_BC_ADD,
                                        'OS_BC_NA': OS_BC_NA,
                                        }
        return ManeuVisionSolutions.objects.filter(id=id).update(content=json.dumps(ManeuVisionSolutions_content))
    except BaseException as msg:
        print(msg)
        return None


def ManeuSubjectiveRefraction_insert(SR_remark='',
                                     OD_Nv='', OD_DS='', OD_CYL='', OD_AX='', OD_NA='', OD_AL='', OD_AC='',
                                     OS_Nv='', OS_DS='', OS_CYL='', OS_AX='', OS_NA='', OS_AL='', OS_AC=''):
    try:
        ManeuSubjectiveRefraction_content = {'SR_remark': SR_remark,
                                             'OD_Nv': OD_Nv, 'OD_DS': OD_DS, 'OD_CYL': OD_CYL, 'OD_AX': OD_AX,
                                             'OD_NA': OD_NA, 'OD_AL': OD_AL, 'OD_AC': OD_AC,
                                             'OS_Nv': OS_Nv, 'OS_DS': OS_DS, 'OS_CYL': OS_CYL, 'OS_AX': OS_AX,
                                             'OS_NA': OS_NA, 'OS_AL': OS_AL, 'OS_AC': OS_AC
                                             }
        return ManeuSubjectiveRefraction.objects.create(content=json.dumps(ManeuSubjectiveRefraction_content))
    except BaseException as msg:
        print(msg)
        return None


def ManeuSubjectiveRefraction_update(id='', SR_remark='',
                                     OD_Nv='', OD_DS='', OD_CYL='', OD_AX='', OD_NA='', OD_AL='', OD_AC='',
                                     OS_Nv='', OS_DS='', OS_CYL='', OS_AX='', OS_NA='', OS_AL='', OS_AC=''):
    try:
        ManeuSubjectiveRefraction_content = {'SR_remark': SR_remark,
                                             'OD_Nv': OD_Nv, 'OD_DS': OD_DS, 'OD_CYL': OD_CYL, 'OD_AX': OD_AX,
                                             'OD_NA': OD_NA, 'OD_AL': OD_AL, 'OD_AC': OD_AC,
                                             'OS_Nv': OS_Nv, 'OS_DS': OS_DS, 'OS_CYL': OS_CYL, 'OS_AX': OS_AX,
                                             'OS_NA': OS_NA, 'OS_AL': OS_AL, 'OS_AC': OS_AC
                                             }
        return ManeuSubjectiveRefraction.objects.filter(id=id).update(
            content=json.dumps(ManeuSubjectiveRefraction_content))
    except BaseException as msg:
        print(msg)
        return None


def ManeuGuess_insert(name='', phone='', sex='', age='', OT='', EM='', DFH='', remark=''):
    try:
        if age == '':
            age = datetime.datetime(2022, 1, 1)
        return ManeuGuess.objects.create(name=name, phone=phone, sex=sex, age=age, ot=OT, em=EM, dfh=DFH, remark=remark)
    except BaseException as msg:
        print(msg)
        return None


def ManeuGuess_update(id='', name='', phone='', sex='', age='', OT='', EM='', DFH='', remark=''):
    try:
        if age == '':
            age = datetime.datetime(2022, 1, 1)
        return ManeuGuess.objects.filter(id=id).update(name=name, phone=phone, sex=sex, age=age, ot=OT, em=EM, dfh=DFH,
                                                       remark=remark)
    except BaseException as msg:
        print(msg)
        return None


def ManeuStore_insert(content):
    try:
        return ManeuStore.objects.create(content=content)
    except BaseException as msg:
        print(msg)
        return None


def ManeuStore_update(arg10="", arg11="", arg12="", arg13="",
                      arg20="", arg21="", arg22="", arg23="",
                      arg30="", arg31="", arg32="", arg33="",
                      arg40="", arg41="", arg42="", arg43="",
                      arg50="", arg51="", arg52="", arg53="",
                      id=''):
    try:
        ManeuStore_content = {'arg50': arg50, 'arg51': arg51, 'arg52': arg52, 'arg53': arg53,
                              'arg40': arg40, 'arg41': arg41, 'arg42': arg42, 'arg43': arg43,
                              'arg30': arg30, 'arg31': arg31, 'arg32': arg32, 'arg33': arg33,
                              'arg20': arg20, 'arg21': arg21, 'arg22': arg22, 'arg23': arg23,
                              'arg10': arg10, 'arg11': arg11, 'arg12': arg12, 'arg13': arg13}
        return ManeuStore.objects.filter(id=id).update(content=json.dumps(ManeuStore_content))
    except BaseException as msg:
        print(msg)
        return None


def ManeuOrderV2_insert(name='', phone='', guess_id='', users_id='', store_id='', visionsolutions_id='', subjectiverefraction_id=''):
    try:
        return ManeuOrderV2.objects.create(name=name, phone=phone, guess_id=guess_id, users_id=users_id,
                                           store_id=store_id, visionsolutions_id=visionsolutions_id,
                                           subjectiverefraction_id=subjectiverefraction_id)
    except BaseException as msg:
        print(msg)
        return None


def ManeuOrderV2_update(order_id='', name='', phone=''):
    try:
        return ManeuOrderV2.objects.filter(id=order_id).update(name=name, phone=phone)
    except BaseException as msg:
        print(msg)
        return None
