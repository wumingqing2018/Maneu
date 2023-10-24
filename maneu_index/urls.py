from django.urls import path

from maneu_index import views
from maneu_index import api

app_name = 'maneu_index'
urlpatterns = [
    # views
    path('', views.index, name='index'),
    path('api_index/', api.index, name='api_index'),
]
