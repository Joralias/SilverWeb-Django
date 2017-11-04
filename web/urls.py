from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^download/$', views.download, name='download'),
    url(r'^store_mail/$', views.new_fan, name='new_fan'),
    url(r'^store_message/$', views.new_message, name='new_message'),
]
