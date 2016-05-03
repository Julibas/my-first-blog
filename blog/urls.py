from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^time$', views.current_datetime),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
