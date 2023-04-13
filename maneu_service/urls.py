from django.urls import path

from maneu_service import views

app_name = 'maneu_service'
urlpatterns = [
    # views
    path('list/', views.list, name='list'),
    path('index/', views.index, name='index'),
    path('insert/', views.insert, name='alterSalesInsert'),
    path('delete/', views.delete, name='alterSalesDelete'),
    path('content/', views.content, name='alterSalesContent'),
]
