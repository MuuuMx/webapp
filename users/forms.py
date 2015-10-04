from django import forms
from django.contrib.auth.models import User

# from .models import BaseUser


class UserForm(forms.ModelForm):

	class Meta():
		model = User
		fields = ['username', 'password', 'email']
