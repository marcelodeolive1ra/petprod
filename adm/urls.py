from django.conf.urls import url
from adm import views

urlpatterns = [
    url(r'^login/$', views.login, name='adm_login'),
    url(r'^logout/$', views.logout, name='adm_logout')
]
