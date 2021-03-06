"""petprod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^medico/', include('medico.urls', namespace='medico')),
    url(r'^modulo/', include('modulo.urls', namespace='modulo')),
    url(r'^adm/', include('adm.urls', namespace='adm')),
    url(r'^emprestimo/', include('emprestimo.urls', namespace='emprestimo')),
    url(r'^classe_social/', include('classe_social.urls', namespace='classe_social')),
    url(r'^area/', include('area.urls', namespace='area')),
    url(r'^evento/', include('evento.urls', namespace='evento')),
    url(r'^cenario/', include('cenario.urls', namespace='cenario')),
    url(r'^rodada/', include('rodada.urls', namespace='rodada')),
    url(r'^Time/', include('Time.urls', namespace='Time')),
]
