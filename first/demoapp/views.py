from django.shortcuts import render
from django.http import HttpResponse
def fun(request):
    message='hello vinoth welcome to django platform'
    return HttpResponse(message)
# Create your views here.
