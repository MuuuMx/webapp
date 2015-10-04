from django.shortcuts import render
from django.shortcuts import get_object_or_404

from users.models import BusinessUser


def home_page(request):

	print(request.user)
	if request.user.is_authenticated():
		try:
			get_object_or_404(BusinessUser, user=request.user)
			return redirect('business:dashboard')
		except:
			return redirect('client:dashboard')
	else:
		return render(request, 'home.html')
