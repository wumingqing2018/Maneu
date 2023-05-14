from django.urls import path

from maneu_service import views

app_name = 'maneu_service'
urlpatterns = [
    # views
    path('index/', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('delete/', views.delete, name='delete'),
    path('content/', views.content, name='content'),
]
