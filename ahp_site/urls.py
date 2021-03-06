"""ahp URL Configuration

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
from django.views.generic import CreateView
from photologue.models import Photo, Gallery

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reports/$', views.report_list, name='reports'),
    url(r'^reports/(?P<report_id>[0-9]+)$', views.report_detail,
        name='report_detail'),
    url(r'^upload/$', CreateView.as_view(model=Gallery, success_url='/', fields='__all__'), name='add-photo')
]
