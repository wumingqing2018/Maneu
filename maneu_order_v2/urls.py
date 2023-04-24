from django.urls import path

from maneu_order_v2 import views

app_name = 'maneu_order_v2'
urlpatterns = [
    # views
    path('index/', views.index, name='index'),
    path('delete/', views.delete, name='delete'),
    path('detail/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('insert/', views.insert, name='insert'),
    path('update/', views.update, name='update'),
    path('test1/', views.test1, name='test'),
]
