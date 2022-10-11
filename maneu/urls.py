from django.conf import settings
from django.conf.urls import url
from django.urls import include
from django.urls import path
from django.views.static import serve

from maneu.views import *

urlpatterns = [
    # 首页
    path('', index, name='index'),
    # 登录页
    path('login/', login, name='login'),
    # 客户页
    path('guess/', guess, name='guess'),
    path('test1/', test1, name='test1'),
    path('test2/', test2, name='test2'),

    # 订单子路由
    path('maneu_order/', include('maneu_order.urls')),
    # 用户子路由
    path('maneu_users/', include('maneu_users.urls')),
    # 批发子路由
    path('maneu_batch/', include('maneu_batch.urls')),
    # 商品子路由
    path('maneu_class/', include('maneu_class.urls')),
]
