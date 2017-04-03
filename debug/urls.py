from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^requirements/$', views.requirements, name='requirements'),
]