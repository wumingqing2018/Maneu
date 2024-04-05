from django.urls import path

from maneu_admin import views

app_name = 'maneu_admin'
urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('insert/', views.user_insert, name='insert'),
    path('updata/', views.user_updata, name='updata'),
    path('detail/', views.user_detail, name='detail'),
]
