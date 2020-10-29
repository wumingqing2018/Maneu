from management import my_lib
from management.models import ProductManage

# Create your service here.


def guest_find_order(order_id, token):
    item = ProductManage.objects.filter(order_id=order_id, token=token).first()
    return item
