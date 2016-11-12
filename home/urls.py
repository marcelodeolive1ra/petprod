from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^base_configuracoes/$', views.base_configuracoes, name='base_configuracoes'),
    url(r'^base_aplicar_dinamica/$', views.base_aplicar_dinamica, name='base_aplicar_dinamica'),
]
