from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.FeatureList.as_view(), name='features'),
	url(r'(?P<pk>[0-9]+)/$', views.FeatureDetail.as_view()),
	url('add', views.FeatureDetail.as_view()),
	url('products/', views.ProductList.as_view()),
	url('clients/', views.ClientList.as_view()),
]