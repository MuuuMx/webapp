from django import forms
from django.contrib.auth.models import User


from .models import BusinessUser


class UserForm(forms.ModelForm):

	class Meta():
		model = User
		fields = ['username', 'password', 'email']


class UserFormLogIn(forms.ModelForm):

	class Meta():
		model = User
		fields = ['username', 'password']


class BusinessUserForm(forms.ModelForm):

	class Meta():
		model = BusinessUser
		fields = ['businessname', 'type']
