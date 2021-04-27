"""maneu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from . import api

app_name = 'order'
urlpatterns = [
    # views
    path('', views.order_list, name='order_list'),
    path('order_detail/', views.order_detail, name='order_detail'),
    path('order_search/', views.order_search, name='order_search'),
    path('order_insert/', views.order_insert, name='order_insert'),
    path('order_update/', views.order_update, name='order_update'),

    # api
    path('api_qr_code/', api.qr_code, name='api_qr_code'),
    path('api_order_insert/', api.order_insert, name='api_order_insert'),
    path('api_order_update/', api.order_update, name='api_order_update'),
    path('api_order_delete/', api.order_delete, name='api_order_delete'),
    path('api_order_list/', api.order_list, name='api_order_list'),
]
