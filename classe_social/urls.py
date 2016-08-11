from django.conf.urls import url
from classe_social import views

urlpatterns = [
    url(r'^$', views.classe_social_index, name='classe_social_index'),
    url(r'^new/$', views.classe_social_new, name='classe_social_new'),
    url(r'^edit/(?P<id>\d+)/$', views.classe_social_edit, name='classe_social_edit'),
    url(r'^delete/(?P<id>\d+)/$', views.classe_social_delete, name='classe_social_delete'),
]