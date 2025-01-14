from django.urls import path

from maneu_admin import views, api

app_name = 'maneu_admin'
urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.user_insert, name='insert'),
    path('api_detail/', api.detail, name='api_detail'),
    path('api_update/', api.update, name='api_update'),
]
