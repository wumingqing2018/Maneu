from django.urls import include
from django.urls import path

from maneu.views import *

urlpatterns = [
    # 首页
    path('', index, name='index'),
    # 登录页
    path('login/', login, name='login'),
    # 用户子路由
    path('maneu_admin/', include('maneu_admin.urls')),
    # 客户子路由
    path('maneu_guest/', include('maneu_guest.urls')),
    # 用户首页子路由
    path('maneu_index/', include('maneu_index.urls')),
    # 售后订单子路由
    path('maneu_service/', include('maneu_service.urls')),
    # 批发订单子路由
    path('maneu_order_v1/', include('maneu_order_v1.urls')),
    # 零售订单子路由
    path('maneu_order_v2/', include('maneu_order_v2.urls')),
]
