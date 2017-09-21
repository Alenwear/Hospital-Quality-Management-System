from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [

    url(r'^registration/', views.registration, name='user_registration'),
    # url(r'^registration/closed/$', views.registration_closed, name='user_registration_closed'),
    # url(r'^registration/complete/$', views.registration_complete, name='user_registration_complete'),
]
