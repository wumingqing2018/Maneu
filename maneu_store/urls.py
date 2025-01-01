from django.urls import path

from maneu_store import api
from maneu_store import views

app_name = 'maneu_store'
urlpatterns = [

    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('insert/', views.insert, name='insert'),
    path('update/', views.update, name='update'),
    path('api_index/', api.index, name='api_index'),
    path('api_detail/', api.detail, name='api_detail'),
    path('api_insert/', api.insert, name='api_insert'),
    path('api_delete/', api.delete, name='api_delete'),
    path('api_search/', api.search, name='api_search'),
]
