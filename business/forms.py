from django import forms
from users.forms import UserForm


class BussinesForm(UserForm):
	address = forms.CharField(max_length=140)
