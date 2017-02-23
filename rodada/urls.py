from django.conf.urls import url
from rodada import views

urlpatterns = [
    url(r'^$', views.rodada_index, name='rodada_index'),
    url(r'^edit/(?P<id>\d+)/$', views.rodada_edit, name='rodada_edit'),
    url(r'^new/$', views.rodada_new, name='rodada_new'),
]
