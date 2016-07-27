from django.conf.urls import url
from medico import views

urlpatterns = [
    url(r'^', views.medico_index, name='medico_index'),
    url(r'^new/$', views.medico_new, name='medico_new'),
]
