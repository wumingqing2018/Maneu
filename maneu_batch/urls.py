from django.urls import path

from maneu_batch import views

app_name = 'maneu_batch'
urlpatterns = [
    # views
    path('index/', views.index, name='index'),
    path('batch_search/', views.batch_search, name='batch_search'),
    path('batch_insert/', views.batch_insert, name='batch_insert'),
    path('batch_delete/', views.batch_delete, name='batch_delete'),
    path('batch_detail/', views.batch_detail, name='batch_detail'),
]
