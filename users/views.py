from django.shortcuts import render, redirect
from django.views.generic import View

# from .models import BaseUser
from .forms import UserForm, UserFormLogIn


class LoginView(View):

	def get(self, request):
		context = {'user_form': UserFormLogIn()}
		print(context['user_form'])
		return render(request, 'login.html', context)


class SignupClientView(View):

	def get(self, request):
		context = {'user_form': UserForm()}
		return render(request, 'signup.html', context)

	def post(self, request):
		user = form.save()
		user.set_password(form.cleaned_data['password'])
		user.save()
		ExtendedUser(user=user, profile_image='', full_name=user.username).save()

		return redirect('home')
