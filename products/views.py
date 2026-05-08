from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
   return HttpResponse("This is the first view of the pylorama")

def products(request):
   return HttpResponse("This is a products page. There should be a form to add products to a table")