from django.urls import path
from maneu_admin import views

app_name = 'maneu_admin'
urlpatterns = [
    path('user_list/', views.user_list, name='user_list'),
    path('user_insert/', views.user_insert, name='user_insert'),
    path('user_updata/', views.user_updata, name='user_updata'),
    path('user_detail/', views.user_detail, name='user_detail'),
]
