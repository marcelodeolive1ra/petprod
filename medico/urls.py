from django.conf.urls import url
from medico import views

urlpatterns = [
    url(r'^$', views.medico_index, name='medico_index'),
    url(r'^edit/(?P<id>\d+)/$', views.medico_edit, name='medico_edit'),
    url(r'^delete/(?P<id>\d+)/$', views.medico_delete, name='medico_delete'),
    url(r'^new/$', views.medico_new, name='medico_new'),
]
