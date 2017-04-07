from django.conf.urls import url
from Time import views

urlpatterns = [
    url(r'^$', views.Time_index, name='time_index'),
    url(r'^new/$', views.Time_new, name='time_new'),
    url(r'^edit/(?P<id>\d+)/$', views.Time_edit, name='time_edit'),
    url(r'^delete/(?P<id>\d+)/$', views.Time_delete, name='time_delete'),
]