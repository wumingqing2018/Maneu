from django.urls import path

from maneu_guest import views

app_name = 'maneu_guest'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('detail/', views.detail, name='detail'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('search/', views.search, name='search'),
    path('Subjective_insert/', views.Subjective_insert, name='Subjective_insert'),
    path('Subjective_detail/', views.Subjective_detail, name='Subjective_detail'),
    path('Subjective_delete/', views.Subjective_delete, name='Subjective_delete'),
    path('Subjective_update/', views.Subjective_update, name='Subjective_update')
]
