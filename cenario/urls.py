from django.conf.urls import url
from cenario import views

urlpatterns = [
    url(r'^$', views.cenario_index, name='cenario_index'),
    url(r'^new/$', views.cenario_new, name='cenario_new'),
    url(r'^edit/(?P<id>\d+)/$', views.cenario_edit, name='cenario_edit'),
    url(r'^delete/(?P<id>\d+)/$', views.cenario_delete, name='cenario_delete'),
]