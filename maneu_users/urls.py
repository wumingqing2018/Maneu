from django.urls import path

from users import api
from users import views

app_name = 'users'
urlpatterns = [
    # view
    path('list/', views.user_list, name='user_list'),
    path('insert/', views.user_insert, name='user_insert'),
    path('update/', views.user_update, name='user_update'),
    path('detail/', views.user_detail, name='user_detail'),

    # api
    path('api_list/', api.user_list, name='api_user_list'),
    path('api_insert/', api.user_insert, name='api_user_insert'),
]
