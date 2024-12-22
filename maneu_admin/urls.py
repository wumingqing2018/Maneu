from django.urls import path

from maneu_admin import views

app_name = 'maneu_admin'
urlpatterns = [
    path('', views.user_list, name='index'),
    path('insert/', views.user_insert, name='insert'),
    path('updata/', views.user_updata, name='update'),
]
