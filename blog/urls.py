from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/(?P<slug>[-\w]+)$', views.view_post, name='view_post'),
	url(r'^category/(?P<slug>[-\w]+)$', views.view_category, name='view_category'),
]
