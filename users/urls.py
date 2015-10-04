from django.conf.urls import patterns, url, include
from .views import client_dashboard, get_business_by_category, search_string, get_search, get_recomendation

urlpatterns = patterns(
	'',
	url(
		r'^$',
		client_dashboard,
		name='dashboard'
	),
	url(
		r'^category/(?P<category>[-\w]{1,144})/$',
		get_business_by_category,
		name='by_category'
	),
	url(
		r'^search/$',
		search_string,
		name='search'
	),
	url(
		r'^search/(?P<search>[-\w]{1,144})/$',
		get_search,
		name='by_category'
	),
	url(
		r'^recomend/$',
		get_recomendation,
		name='search'
	),
)
