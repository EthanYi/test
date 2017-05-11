from django.shortcuts import render

# Create your views here.
def home(request):
	string = request.GET['a']
	return render(request, 'testapp1/home.html', {'string': string})
