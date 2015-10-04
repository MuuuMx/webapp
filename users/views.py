import urllib
import json
import random

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

# from .models import BaseUser
from .forms import UserForm, UserFormLogIn, BusinessUserForm, categories_of_business
from business.models import Place, Product
from .models import BusinessUser


def logout_user(request):
	logout(request)
	return redirect('home')


def get_recomendation(request):
	place = random.choice(Place.objects.all())
	context = {
			'user_type': False,
			'categories': categories_of_business,
			'place_recomended': place
		}
	return render(request, 'news.html', context)


def search_string(request):
	string_to_search = request.POST['search']
	return redirect('/client/search/%s/' % string_to_search)


def get_search(request, search):
	results = Product.objects.filter(name__icontains=search)
	print(results)
	context = {
		'user_type': False,
		'categories': categories_of_business,
		'results': results
	}
	return render(request, 'news.html', context)


def client_dashboard(request):
	context = {
		'user_type': False,
		'categories': categories_of_business
	}
	return render(request, 'news.html', context)


def get_business_by_category(request, category=''):
	places = [business.place_set.all()[0] for business in BusinessUser.objects.filter(type=category)]

	print(places)
	context = {
		'user_type': False,
		'categories': categories_of_business,
		'results': False,
		'places_category': True,
		'places': places
	}
	return render(request, 'news.html', context)


class LoginView(View):

	def get(self, request):
		context = {'user_form': UserFormLogIn()}
		print(context['user_form'])
		return render(request, 'login.html', context)

	def post(self, request):
		print(request.POST['username'])
		print(request.POST['password'])
		user = authenticate(
			username=request.POST['username'],
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
			user.set_password(request.POST['password'])
			user.save()
			# print(user.password, user.name)
			user = authenticate(
				username=request.POST['username'],
				password=request.POST['password']
			)
			# print(user)
			login(request, user)

		except Exception as e:
			print(e)

		return redirect('home')


class SignupBusinessView(View):

	def get(self, request):
		context = {
			'user_form': UserForm(),
			'business_form': BusinessUserForm()
		}
		return render(request, 'signup.html', context)

	def post(self, request):
		try:
			user = UserForm(request.POST, request)
			if user.is_valid():
				user = user.save()
				user.set_password(request.POST['password'])
				user.save()
				print(user)
				user = authenticate(username=user.username, password=request.POST['password'])
				login(request, user)
			else:
				print(user.errors.items())
				user.pk

			business_user = BusinessUserForm(request.POST, request.FILES).save(commit=False)
			business_user.user = user
			business_user.save()

			address = request.POST['address'].replace(' ', '+')

			f = urllib.request.urlopen(
				"https://maps.googleapis.com/maps/api/geocode/json?"
				+ "address=%s&key=%s" % (
					address, 'AIzaSyDvWO5mvLcP3pqdb9c6gXCsW5IyZta2rdA'
				)
			).read().decode()

			latlon = json.loads(f)['results'][0]['geometry']['location']
			address = request.POST['address'].replace('+', ' ')
			place = Place(
				business_user=business_user,
				address=address,
				longitude=latlon['lng'],
				latitude=latlon['lat']
			).save()

		except Exception as e:
			print(e)

		return redirect('home')


