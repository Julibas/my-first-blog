from django.conf.urls import patterns, url
from . import views

urlpatterns = [
	url(r'^start$', views.start),
	url(r'^data$', views.work_data),
	url(r'^all_contacts$', views.all_contacts),

]