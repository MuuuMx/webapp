from django.shortcuts import render
from django.shortcuts import get_object_or_404


def home_page(request):

	if request.user.is_authenticated():
		return render(request, 'news.html')

	else:
		return render(request, 'home.html')
