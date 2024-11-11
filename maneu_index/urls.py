from django.urls import path

from maneu_index import api
from maneu_index import views

app_name = 'maneu_index'
urlpatterns = [
    # views
    path('index1/', views.index1, name='index1'),
    path('index2/', views.index2, name='index2'),

    path('api_index/', api.index, name='api_index'),
    path('api_index/', api.index, name='api_index'),
]
