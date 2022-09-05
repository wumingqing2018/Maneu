from common import common
from maneu_order.models import ManeuUsers
from maneu_order.models import ManeuGuess
from maneu_order.models import ManeuStore
from maneu_order.models import ManeuOrder
from maneu_order.models import ManeuOrderV2
from maneu_order.models import ManeuVisionSolutions
from maneu_order.models import ManeuSubjectiveRefraction

import json, datetime


def order_insert(form):
    """
    添加订单
    """
    try:
        item = ManeuOrder.objects.create(
            # 订单
            order_id=common.create_id(),
            order_token=common.token(),
            # 客户
            c_name=form['c_name'],
            c_phone=form['c_phone'],
            c_time=common.current_time(),
            # 商家
            besiness='',
            order=form['order'],
            # 备注
            remark=form['remark'],
        )
        return item
    except BaseException as msg:
        print(msg)
        return None


def order_update(id, form):
    """更新订单"""
    try:
        order = ManeuOrder.objects.filter(id=id)
        order.update(c_name=form.data['c_name'],
                     c_phone=form.data['c_phone'],
                     c_time=common.current_time(),
                     # 商家
                     besiness='',
                     # 镜架
                     frame=form.data['frame'],
                     # 左眼
                     l_glasses=form.data['l_glasses'],
                     l_pd=form.data['l_pd'],
                     l_add=form.data['l_add'],
                     l_sphere=form.data['l_sphere'],
                     l_deviation=form.data['l_deviation'],
                     l_astigmatic=form.data['l_astigmatic'],
                     # 右眼
                     r_glasses=form.data['r_glasses'],
                     r_pd=form.data['r_pd'],
                     r_add=form.data['r_add'],
                     r_sphere=form.data['r_sphere'],
                     r_astigmatic=form.data['r_astigmatic'],
                     r_deviation=form.data['r_deviation'],
                     # 备注
                     todo=form.data['todo'],
                     )
        return order
    except BaseException as msg:
        print(msg)
        return None


def order_delete(id):
    """删除订单"""
    try:
        order = ManeuOrder.objects.filter(id=id).all()
        order.delete()
        return True
    except BaseException as msg:
        print(msg)
        return False


def find_order_all():
    """
    全部订单
    """
    try:
        return ManeuOrderV2.objects.order_by('-time').all()
    except BaseException as msg:
        print(msg)
        return None


def find_order_name(name):
    try:
        return ManeuOrder.objects.filter(c_name=name).order_by('-c_time').all()
    except BaseException as msg:
        print(msg)
        return None


def find_order_today():
    """
    查找今日订单
    根据时间排序
    """
    try:
        today = common.today()
        return ManeuOrder.objects.filter(c_time__gt=today)
    except BaseException as msg:
        return msg


def find_order_id(order_id):
    """
    查找指定订单
    根据时间排序
    """
    try:
        return ManeuOrderV2.objects.filter(id=order_id).first()
    except BaseException as msg:
        print(msg)
        return None


def delete_order_id(id=''):
    """
    查找指定订单
    根据时间排序
    """
    try:
        order = ManeuOrderV2.objects.filter(id=id).all()
        return order.delete()
    except BaseException as msg:
        print(msg)
        return None


def find_order_id_token(order_id, token):
    """
    查找指定订单
    根据时间排序
    """
    try:
        return ManeuOrder.objects.filter(order_id=order_id, order_token=token).first()
    except BaseException as msg:
        print(msg)
        return None


def find_order_phone(phone=''):
    try:
        return ManeuOrderV2.objects.filter(phone=phone).order_by('-time').all()
    except BaseException as msg:
        print(msg)
        return None


def find_order_name(name):
    try:
        return ManeuOrder.objects.filter(c_name=name).all()
    except BaseException as msg:
        print(msg)
        return None


def find_order_time(time):
    try:
        return ManeuOrder.objects.filter(c_time__gt=time).all()
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


def ManeuGuess_insert(name='', phone='', sex='', age='', OT='', EM='', DFH='', remark=''):
    try:
        if age == '':
            age = datetime.datetime(2022, 1, 1)
        return ManeuGuess.objects.create(name=name, phone=phone, sex=sex, age=age, ot=OT, em=EM, dfh=DFH, remark=remark)
    except BaseException as msg:
        print(msg)
        return None


def ManeuStore_insert(arg51='', arg52='', arg53='', arg41='', arg42='', arg43='', arg31='', arg32='', arg33='',
                      arg21='', arg22='', arg23='', arg11='', arg12='', arg13='', ):
    try:
        ManeuStore_content = {'arg51': arg51, 'arg52': arg52, 'arg53': arg53, 'arg41': arg41, 'arg42': arg42,
                              'arg43': arg43, 'arg31': arg31, 'arg32': arg32, 'arg33': arg33, 'arg21': arg21,
                              'arg22': arg22, 'arg23': arg23, 'arg11': arg11, 'arg12': arg12, 'arg13': arg13, }
        return ManeuStore.objects.create(content=json.dumps(ManeuStore_content))
    except BaseException as msg:
        print(msg)
        return None


def ManeuOrderV2_insert(name='', phone='', guess_id='', users_id='', store_id='', visionsolutions_id='',
                        subjectiverefraction_id=''):
    try:
        return ManeuOrderV2.objects.create(name=name, phone=phone, guess_id=guess_id, users_id=users_id,
                                           store_id=store_id, visionsolutions_id=visionsolutions_id,
                                           subjectiverefraction_id=subjectiverefraction_id)
    except BaseException as msg:
        print(msg)
        return None
