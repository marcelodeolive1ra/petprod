from django.conf.urls import url
from modulo import views

urlpatterns = [
    url(r'^$', views.modulo_index, name='modulo_index'),
    url(r'^new/$', views.modulo_new, name='modulo_new'),
    url(r'^edit/(?P<id>\d+)/$', views.modulo_edit, name='modulo_edit'),
    url(r'^delete/(?P<id>\d+)/$', views.modulo_delete, name='modulo_delete'),
]