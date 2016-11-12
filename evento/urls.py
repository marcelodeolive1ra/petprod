from django.conf.urls import url
from evento import views

urlpatterns = [
    url(r'^$', views.evento_index, name='evento_index'),
    url(r'^new/$', views.evento_new, name='evento_new'),
    url(r'^edit/(?P<id>\d+)/$', views.evento_edit, name='evento_edit'),
    url(r'^delete/(?P<id>\d+)/$', views.evento_delete, name='evento_delete'),
]