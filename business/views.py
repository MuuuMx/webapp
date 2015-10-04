from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .forms import ProductForm, MaterialForm
from .models import Product, Material, Sale


def business_dashboard(request):
	context = {'user_type': True}
	return render(request, 'dashboard.html', context)


def business_graphic(request):
	context = {
		'user_type': True,
		'func': 'resumen'
	}
	return render(request, 'dashboard.html', context)


def business_stock(request):
	context = {
		'user_type': True,
		'func': 'stock',
		'materials': Material.objects.all()
	}
	return render(request, 'dashboard.html', context)


def business_products(request):
	context = {
			'user_type': True,
			'func': 'catalogo',
			'products': Product.objects.all()
		}
	return render(request, 'dashboard.html', context)


class SalesView(View):
	def get(self, request):
		context = {
			'products': Product.objects.all(),
			'user_type': True,
			'func': 'ventas'
		}
		return render(request, 'dashboard.html', context)

	def post(self, request):
		products = request.POST.getlist('checks')

		print(request.POST['quantity%s' % 3])

		for i in products:
			Sale(
				quantity=request.POST['quantity%s' % i],
				product=get_object_or_404(Product, pk=i),
			).save()
		print(products)

		return redirect('business:sales')




class AddProductView(View):
	def get(self, request):
		context = {
			'user_type': True,
			'func': 'product',
			'product_form': ProductForm(),
			'material_form': MaterialForm()
		}
		return render(request, 'dashboard.html', context)

	def post(self, request):
		product = ProductForm(request.POST, request.FILES).save()

		counter = 1
		for i in range(1, 11):
			if request.POST.get('name%s' % i, ''):
				info = {
					'name': request.POST['name%s' % i],
					'unity': request.POST['unity%s' % i],
					'quantity': request.POST['quantity%s' % i],
					'cost': request.POST['cost%s' % i],
				}
				material = MaterialForm(info, {}).save(commit=False)
				material.product = product
				material.save()

		return redirect('business:add_product')
