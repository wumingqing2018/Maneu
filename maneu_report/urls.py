from django.urls import path
from maneu_report import api


app_name = 'maneu_report'
urlpatterns = [
    # views
    path('api_detail/', api.detail, name='api_detail'),
]
