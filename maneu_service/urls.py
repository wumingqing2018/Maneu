from django.urls import path

from maneu_service import tests
from maneu_service import views

app_name = 'maneu_service'
urlpatterns = [
    # views
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('delete/', views.delete, name='delete'),
]
