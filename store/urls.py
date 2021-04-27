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
    # glass_views
    path('store/', views.store, name='store'),
    path('glass_store/', views.glass_store_all, name='glass_store'),
    path('glass_content/', views.glass_content, name='glass_content'),
    path('glass_insert/', views.glass_insert, name='glass_insert'),
    # framework_views
    path('framework_find/', views.framework_find, name='framework_find'),
    path('framework_store/', views.framework_list, name='framework_store'),
    path('framework_insert/', views.framework_insert, name='framework_insert'),

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
