from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
	url(r'^detail/(?P<pk>\w+)/$', views.detail, name = 'product_detail'),
    url(r'^', views.products, name = 'products'),

]