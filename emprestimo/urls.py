from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.emprestimo_index, name='emprestimo_index'),
    url(r'^delete/(?P<id>\d+)/$', views.emprestimo_delete, name='emprestimo_delete'),
    url(r'^edit/(?P<id>\d+)/$', views.emprestimo_edit, name='emprestimo_edit'),
    url(r'^new/$', views.emprestimo_new, name='emprestimo_new'),
]