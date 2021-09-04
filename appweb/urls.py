from django.urls import path 
from django.conf.urls import url

from . import views 

app_name = 'appweb'

urlpatterns = [
    url(r'^detail/(?P<detail_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),
    url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),

]
