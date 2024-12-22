from django.urls import path

from maneu_store import api

app_name = 'maneu_store'
urlpatterns = [
    path('api_insert/', api.insert, name='api_insert')
]
