#coding:utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def old_add2_redirect(request, a, b):
	return HttpResponseRedirect(
		reverse('add1', args=(a, b))
	)

def index(request):
	return render(request, 'testapp1/home.html')

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a)+int(b)
	return HttpResponse(str(c))

def add1(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
