from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^check', views.check, name='check'),
    url(r'^showchecks/$', views.showchecks, name='showchecks'),
    url(r'^success/$', views.success, name='success'),
]
