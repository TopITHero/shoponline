from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^buying/$', views.buying, name = 'buying'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete_product, name = 'delete')
]