from django.conf.urls import url

from . import views

app_name = 'debug'
urlpatterns = [
    url(r'^requirements/$', views.requirements),
]
