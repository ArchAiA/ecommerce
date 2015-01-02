from django.shortcuts import render

# Create your views here.

def home(request):

	if request.user.is_authenticated():	
		context = {'username_is': request.user}
	else:
		context = {'username_is': request.user}

	template = 'base.html'
	
	return render(request, template, context)