from django.urls import path
from . import views
from . import api

app_name = 'user'
urlpatterns = [
    # view
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('list/', views.user_list, name='user_list'),
    path('content/', views.user_content, name='content'),
    path('insert/', views.user_insert, name='insert'),
    path('update/', views.user_update, name='update'),

    # api
    path('api_list/', api.user_list, name='api_list'),
    path('api_login/', api.user_login, name='api_login'),
    path('api_insert/', api.user_insert, name='api_insert'),
    path('api_freeze/', api.user_freeze, name='api_freeze'),
    path('api_unfreeze/', api.user_unfreeze, name='api_unfreeze'),
]
