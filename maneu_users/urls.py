from django.urls import path

from maneu_users import api
from maneu_users import views

app_name = 'maneu_users'
urlpatterns = [
    # view
    path('user_list/', views.user_list, name='user_list'),
    path('insert/', views.user_insert, name='user_insert'),
    path('update/', views.user_update, name='user_update'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('user_delete/', views.user_delete, name='user_delete'),

    # api
    path('api_user_list/', api.user_list, name='api_user_list'),
    path('api_user_insert/', api.user_insert, name='api_user_insert'),
    path('api_user_update/', api.user_insert, name='api_user_update'),

]
