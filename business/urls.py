from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns(
	'',
	url(
		r'^$',
		views.business_dashboard,
		name='dashboard'
	),
	url(
		r'^graphic/$',
		views.business_graphic,
		name='graphic'
	),
	url(
		r'^sales/$',
		views.SalesView.as_view(),
		name='sales'
	),
	url(
		r'^sales_month/$',
		views.sales_month,
		name='sales'
	),
	#ya
	url(
		r'^add_product/$',
		views.AddProductView.as_view(),
		name='add_product'
	),
	url(
		r'^stock/$',
		views.business_stock,
		name='stock'
	),
	#ya
	url(
		r'^products/$',
		views.business_products,
		name='products'
	),
)
