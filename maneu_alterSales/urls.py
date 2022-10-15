from django.urls import path
from maneu_alterSales import views

app_name = 'maneu_alterSales'
urlpatterns = [
    # views
    path('alterSalesindex/', views.alterSalesindex, name='alterSalesindex'),
    path('alterSalesList/', views.alterSales_List, name='alterSalesList'),
    path('alterSalesInsert/', views.alterSales_insert, name='alterSalesInsert'),
    path('alterSalesDelete/', views.alterSales_delete, name='alterSalesDelete'),
    path('alterSalesContent/', views.alterSales_content, name='alterSalesContent'),
]
