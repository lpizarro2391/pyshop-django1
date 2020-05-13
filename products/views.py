from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# / productos - index
# Uniform Resource Locator (Adress)
def index(request):
    products = Product.objets.all()
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Products')

