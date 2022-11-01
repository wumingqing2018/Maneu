from django.urls import path

from maneu_client import views

app_name = 'maneu_client'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('detail/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]
