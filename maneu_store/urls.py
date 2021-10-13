from django.urls import path

from maneu_store import api
from maneu_store import views

app_name = 'maneu_store'
urlpatterns = [
    # index
    path('store_list/', views.store_list, name='store_list'),
    path('store_insert/', views.store_insert, name='store_insert'),
]
