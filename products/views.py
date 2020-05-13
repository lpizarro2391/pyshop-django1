from django.http import HttpResponse
from django.shortcuts import render

# / productos - index
# Uniform Resource Locator (Adress)
def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Products')

