from django.urls import path

from maneu_class import views

app_name = 'maneu_class'

urlpatterns = [
    path('class_list/', views.class_list, name='class_list'),
    path('class_insert/', views.class_insert, name='class_insert'),
]
