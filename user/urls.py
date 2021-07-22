from django.urls import path

from user import api
from user import views

app_name = 'user'
urlpatterns = [
    # view
    path('list/', views.user_list, name='user_list'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('insert/', views.user_insert, name='user_insert'),
    path('update/', views.user_update, name='user_update'),
    path('detail/', views.user_detail, name='user_detail'),

    # api
    path('api_list/', api.user_list, name='api_user_list'),
    path('api_insert/', api.user_insert, name='api_user_insert'),
    path('api_freeze/', api.user_freeze, name='api_user_freeze'),
    path('api_unfreeze/', api.user_unfreeze, name='api_user_unfreeze'),
]
