from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Myfirstview(request):
    return HttpResponse("<h1 style='color:red'>welcome to django<h1>")