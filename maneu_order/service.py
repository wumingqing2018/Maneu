from common import common
from maneu_order.models import Order


def order_insert(form):
    """
    添加订单
    """
    try:
        item = Order.objects.create(
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
        order = Order.objects.filter(id=id)
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
        order = Order.objects.filter(id=id).all()
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
        return Order.objects.order_by('-c_time').all()
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
        return Order.objects.filter(c_time__gt=today)
    except BaseException as msg:
        return msg


def find_order_id(order_id):
    """
    查找指定订单
    根据时间排序
    """
    try:
        return Order.objects.filter(order_id=order_id).first()
    except BaseException as msg:
        print(msg)
        return None


def find_order_id_token(order_id, token):
    """
    查找指定订单
    根据时间排序
    """
    try:
        return Order.objects.filter(order_id=order_id, order_token=token).first()
    except BaseException as msg:
        print(msg)
        return None


def find_order_phone(phone):
    try:
        return Order.objects.filter(c_phone=phone).all()
    except BaseException as msg:
        print(msg)
        return None


def find_order_name(name):
    try:
        return Order.objects.filter(c_name=name).all()
    except BaseException as msg:
        print(msg)
        return None


def find_order_time(time):
    try:
        return Order.objects.filter(c_time__day=time).all()
    except BaseException as msg:
        print(msg)
        return None
