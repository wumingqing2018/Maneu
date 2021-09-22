from django.conf import settings
from django.conf.urls import url
from django.urls import path
from django.views.static import serve

from maneu_batch import views

app_name = 'maneu_batch'
urlpatterns = [
    # views
    path('batch_list/', views.batch_list, name='batch_list'),
    path('batch_insert/', views.batch_insert, name='batch_insert'),
    path('batch_delete/', views.batch_delete, name='batch_delete'),
    path('batch_detail/', views.batch_detail, name='batch_detail'),
    url(r'batch_detail/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})
]
