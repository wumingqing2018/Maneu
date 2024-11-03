from django.urls import path

from maneu_order import api
from maneu_order import views

app_name = 'maneu_order'
urlpatterns = [
    # views
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('insert/', views.insert, name='insert'),
    path('update/', views.update, name='update'),
    path('api_index/', api.index, name='api_index'),
    path('api_insert/', api.insert, name='api_insert'),
    path('api_delete/', api.delete, name='api_delete'),
    path('api_search/', api.search, name='api_search'),
    path('service_insert/', api.service_insert, name='service_insert'),
    path('service_delete/', api.service_delete, name='service_delete'),
    path('service_update/', api.service_update, name='service_update'),
]
