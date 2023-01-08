from django.urls import path

from guess import views

app_name = 'guess_admin'
urlpatterns = [
    # views
    path('order_list/', views.order_list, name='order_list'),
    path('order_detail/', views.order_detail, name='order_detail'),
]
