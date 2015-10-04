from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login

# from .models import BaseUser
from .forms import UserForm, UserFormLogIn


class LoginView(View):

	def get(self, request):
		context = {'user_form': UserFormLogIn()}
		print(context['user_form'])
		return render(request, 'login.html', context)

	def post(self, request):
		print(request.POST['username'])
		print(request.POST['password'])
		user = authenticate(
			user=request.POST['username'],
			password=request.POST['password']
		)
		print(user)
		login(request, user)

		return redirect('home')


class SignupClientView(View):

	def get(self, request):
		context = {'user_form': UserForm()}
		return render(request, 'signup.html', context)

	def post(self, request):
		try:
			user = UserForm(request.POST, request).save()
			user.set_password(form.cleaned_data['password'])
			user.save()
			ExtendedUser(user=user, profile_image='', full_name=user.username).save()

			user = authenticate(user=user.username, password=user.password)
			login(request, user)

		except Exception as e:
			print(e)

		return redirect('home')
