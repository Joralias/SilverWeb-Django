from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index', views.index, name='index'),
    url(r'^about', views.about),
    url(r'^contact', views.contact),
    url(r'^gallery', views.gallery),
    url(r'^blog', views.blog),
    url(r'^download', views.download),
    url(r'^store_mail', views.new_fan, name='new_fan'),
    url(r'^store_message', views.new_message, name='new_message'),
]