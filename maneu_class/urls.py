from django.urls import path

from maneu_class import views

app_name = 'maneu_class'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('class_insert/', views.class_insert, name='class_insert'),
]
