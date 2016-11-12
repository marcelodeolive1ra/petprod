from django.conf.urls import url
from area import views

urlpatterns = [
    url(r'^$', views.area_index, name='area_index'),
    url(r'^new/$', views.area_new, name='area_new'),
    url(r'^edit/(?P<id>\d+)/$', views.area_edit, name='area_edit'),
    url(r'^delete/(?P<id>\d+)/$', views.area_delete, name='area_delete'),
]