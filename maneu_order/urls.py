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
    path('index/', api.index, name='api_index'),
    path('delete/', api.delete, name='api_delete'),
    path('search/', api.search, name='api_search'),
    path('service_insert/', api.service_insert, name='service_insert'),
    path('service_delete/', api.service_delete, name='service_delete')
]
