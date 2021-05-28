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

app_name = 'store'
urlpatterns = [
    # index
    path('list/', views.store, name='list'),
    # glass_views
    path('glass_list/', views.glass_list, name='glass_list'),
    path('glass_insert/', views.glass_insert, name='glass_insert'),
    path('glass_content/', views.glass_content, name='glass_content'),
    # framework_views
    path('framework_list/', views.framework_list, name='framework_list'),
    path('framework_insert/', views.framework_insert, name='framework_insert'),
    path('framework_content/', views.framework_content, name='framework_content'),

    # glass_api
    path('api_glass_insert/', api.glass_insert, name='api_glass_insert'),
    path('api_glass_store_brand/', api.glass_store_brand, name='api_glass_store_brand'),
    path('api_glass_store_model/', api.glass_store_model, name='api_glass_store_model'),
    path('api_glass_store_sphere/', api.glass_store_sphere, name='api_glass_store_sphere'),
    path('api_glass_store_astigmatic/', api.glass_store_astigmatic, name='api_glass_store_astigmatic'),
    path('api_glass_store_refraction/', api.glass_store_refraction, name='api_glass_store_refraction'),
    path('api_glass_store_count/', api.glass_store_count, name='api_glass_store_count'),
    # framework_api
    path('api_framework_insert/', api.framework_insert, name='api_framework_insert'),
    path('api_framework_store_brand/', api.framework_store_brand, name='api_framework_store_brand'),
    path('api_framework_store_model/', api.framework_store_model, name='api_framework_store_model'),
    path('api_framework_store_count/', api.framework_store_count, name='api_framework_store_count'),
]
