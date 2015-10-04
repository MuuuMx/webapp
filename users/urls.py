from django.conf.urls import patterns, url, include
from .views import client_dashboard

urlpatterns = patterns(
	'',
	url(
		r'^$',
		client_dashboard,
		name='dashboard'
	),
)
