from django.urls import include, path
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.views.generic import TemplateView
from features import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='login.html'), name="home"),
	url('featurescreen', TemplateView.as_view(template_name='listing.html'), name="home"),
	url('addscreen', TemplateView.as_view(template_name='AddList.html')),
    path('features/', include('features.urls')),
    path('admin/', admin.site.urls),
	url(r'^api-token-auth', obtain_jwt_token, name="api-token-auth"),
	url('viewscreen/(?P<pk>[0-9]+)/', views.ViewScreen.as_view()),
]