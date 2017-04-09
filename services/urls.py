from django.conf.urls import include, url
from django.contrib import admin
from services import views

urlpatterns = [
	url(r'^$',views.service_list,name='service'),
]