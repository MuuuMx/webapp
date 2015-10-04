from django.shortcuts import render
from django.views.generic import View


def business_dashboard(request):
	context = {'user_type': True}
	return render(request, 'dashboard.html', context)


def business_graphic(request):
	context = {}
	return render(request, 'dashboard.html')


def business_stock(request):
	context = {}
	return render(request, 'dashboard.html')


def business_products(request):
	context = {}
	return render(request, 'dashboard.html')


class SalesView(View):
	def get(self, request):
		return render(request, 'dashboard.html', context)


class AddProductView(View):
	def get(self, request):
		return render(request, 'dashboard.html', context)
