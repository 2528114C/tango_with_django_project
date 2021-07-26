from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    str = "<a href='/rango/about/'>About</a>"
    return HttpResponse("Rango says hey there partner"+str)
def about(request):
    str = "<a href='/rango/'>Index</a>"
    return HttpResponse("Rango says here is the about page."+str)