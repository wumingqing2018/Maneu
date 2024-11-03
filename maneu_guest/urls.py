from django.urls import path

from maneu_guest import views, api

app_name = 'maneu_guest'

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('detail/', views.detail, name='detail'),
    path('update/', views.update, name='update'),
    path('Subjective_insert/', views.Subjective_insert, name='Subjective_insert'),
    path('Subjective_detail/', views.Subjective_detail, name='Subjective_detail'),
    path('Subjective_delete/', views.Subjective_delete, name='Subjective_delete'),
    path('Subjective_update/', views.Subjective_update, name='Subjective_update'),
    path('api_index/', api.index, name='api_index'),
    path('api_search/', api.search, name='api_search'),
    path('api_delete/', api.delete, name='api_delete'),

]
