from django.urls import path

from maneu_guest import views, api

app_name = 'maneu_guest'

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('detail/', views.detail, name='detail'),
    path('update/', views.update, name='update'),
    path('api_index/', api.index, name='api_index'),
    path('api_search/', api.search, name='api_search'),
    path('api_insert/', api.insert, name='api_insert'),
    path('api_delete/', api.delete, name='api_delete'),
    path('api_detail/', api.detail, name='api_detail'),
    path('api_update/', api.update, name='api_update'),
]
