from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from users.models import BusinessUser
from django.contrib.auth.models import User


def home_page(request):

	print(request.user)
	if request.user.is_authenticated():
		try:
			print(request.user.pk)
			get_object_or_404(BusinessUser, user=request.user.pk)
			return redirect('business:dashboard')
		except Exception as e:
			print(e)
			return redirect('client:dashboard')
	else:
		return render(request, 'home.html')
