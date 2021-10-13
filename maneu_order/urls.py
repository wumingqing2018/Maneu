from django.urls import path

from maneu_order import api
from maneu_order import views

app_name = 'maneu_order'
urlpatterns = [
    # views
    path('order_list/', views.order_list, name='order_list'),
    path('order_detail/', views.order_detail, name='order_detail'),
    path('order_search/', views.order_search, name='order_search'),
    path('order_insert/', views.order_insert, name='order_insert'),
    path('order_update/', views.order_update, name='order_update'),
    # api
    path('api_order_list/', api.order_list, name='api_order_list'),
    path('api_order_qrcode/', api.order_qrcode, name='api_order_qrcode'),
    path('api_order_detail/', api.order_detail, name='api_order_detail'),
    path('api_order_insert/', api.order_insert, name='api_order_insert'),
    path('api_order_update/', api.order_update, name='api_order_update'),
    path('api_order_delete/', api.order_delete, name='api_order_delete'),
]
