from django.urls import path

from store import api
from store import views

app_name = 'store'
urlpatterns = [
    # index
    path('store_list/', views.store_list, name='store_list'),
    # glass_views
    path('glass_list/', views.glass_list, name='glass_list'),

    path('glass_insert/', views.glass_insert, name='glass_insert'),
    path('glass_content/', views.glass_detail, name='glass_content'),
    # framework_views
    path('framework_list/', views.framework_list, name='framework_list'),
    path('framework_insert/', views.framework_insert, name='framework_insert'),
    path('framework_content/', views.framework_detail, name='framework_content'),

    # glass_api
    path('api_glass_count/', api.glass_count, name='api_glass_count'),
    path('api_glass_brand/', api.glass_brand, name='api_glass_brand'),
    path('api_glass_model/', api.glass_model, name='api_glass_model'),
    path('api_glass_insert/', api.glass_insert, name='api_glass_insert'),
    path('api_glass_sphere/', api.glass_sphere, name='api_glass_sphere'),
    path('api_glass_astigmatic/', api.glass_astigmatic, name='api_glass_astigmatic'),
    path('api_glass_refraction/', api.glass_refraction, name='api_glass_refraction'),
    # framework_api
    path('api_framework_insert/', api.framework_insert, name='api_framework_insert'),
    path('api_framework_brand/', api.framework_brand, name='api_framework_brand'),
    path('api_framework_model/', api.framework_model, name='api_framework_model'),
    path('api_framework_count/', api.framework_count, name='api_framework_count'),

    # store
    path('store_insert/', views.store_insert, name='store_insert'),
]
