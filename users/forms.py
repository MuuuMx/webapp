from django import forms
from django.contrib.auth.models import User


from .models import BusinessUser

categories_of_business = [
	'Abarrotes',
	'Comida',
	'Medicina y salud',
	'Cultura',
	'Hospedaje',
	'Entretenimiento',
	# 'Servicios profesionales'
]


class UserForm(forms.ModelForm):

	class Meta():
		model = User
		fields = ['username', 'password', 'email']

		labels = {
			'username': 'Nombre de usuario',
			'password': 'Contraseña',
			'email': 'Correo electronico'
		}

		widgets = {
			'password': forms.PasswordInput(
				attrs={
					'type': 'password',
					'class': 'input_field input_field-social',
					'placeholder': 'Ingresa tu contraseña'}
			)
		}


class UserFormLogIn(forms.ModelForm):

	class Meta():
		model = User
		fields = ['username', 'password']

		widgets = {
			'password': forms.PasswordInput(
				attrs={
					'type': 'password',
					'class': 'input_field input_field-social',
					'placeholder': 'Ingresa tu contraseña'}
			)
		}


class BusinessUserForm(forms.ModelForm):

	class Meta():
		model = BusinessUser
		fields = ['businessname', 'type']
