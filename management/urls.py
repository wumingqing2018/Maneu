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
from management import views

urlpatterns = [
    path('add_order/', views.add_order, name='add_order'),
    path('order_list', views.order_list, name='order_list'),
    path('check_order/', views.check_order, name='check_order'),
    path('find_order/', views.find_order, name='find_order'),
    path('delete_order/', views.delete_order, name='delete_order'),
    path('update_order/', views.update_order, name='update_order'),
    path('QR_code/', views.qr_code_api, name='QR_code'),
    path('guest_find_order/<int:id>/<int:token>/', views.find_order),
]
