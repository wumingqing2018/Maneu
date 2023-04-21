from django.urls import path

from maneu_service import views

app_name = 'maneu_service'
urlpatterns = [
    # views
    path('index1/', views.index1, name='index1'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    path('insert/', views.insert, name='insert'),
    path('delete/', views.delete, name='delete'),
    path('content/', views.content, name='content'),
]
