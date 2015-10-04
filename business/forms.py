from django import forms
from users.forms import UserForm

from .models import Product, Material, Sale


class ProductForm(forms.ModelForm):

	class Meta():
		model = Product
		exclude = ['business']

		labels = {
			'name': 'Nombre del producto',
			'price': 'Precio al que se vende',
			'quantity': 'Cantidad en stock'
		}


class MaterialForm(forms.ModelForm):

	class Meta():
		model = Material
		exclude = ['product']
