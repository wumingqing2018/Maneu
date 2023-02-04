from django.urls import path

from maneu_alterSales import views

app_name = 'maneu_alterSales'
urlpatterns = [
    # views
    path('index/', views.index, name='index'),
    path('alterSalesList/', views.list, name='alterSalesList'),
    path('alterSalesInsert/', views.insert, name='alterSalesInsert'),
    path('alterSalesDelete/', views.delete, name='alterSalesDelete'),
    path('alterSalesContent/', views.content, name='alterSalesContent'),
    path('error/', views.error, name='error')
]
