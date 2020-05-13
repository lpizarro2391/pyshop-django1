from django.http import HttpResponse
from django.shortcuts import render

# / productos - index
# Uniform Resource Locator (Adress)
def index(requests):
    return HttpResponse('Hello Wold')

