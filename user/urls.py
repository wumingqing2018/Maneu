"""
maneu URL Configuration

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

app_name = 'user'
urlpatterns = [
    # view
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_find/', views.user_find, name='user_find'),
    path('user_insert/', views.user_insert, name='user_insert'),
    path('user_update/', views.user_update, name='user_update'),

    # api
    path('api_list/', api.user_list, name='api_list'),
    path('api_login/', api.login, name='api_login'),
    path('api_insert/', api.user_insert, name='api_insert'),
    path('api_freeze/', api.user_freeze, name='api_freeze'),
    path('api_unfreeze/', api.user_unfreeze, name='api_unfreeze'),
]
