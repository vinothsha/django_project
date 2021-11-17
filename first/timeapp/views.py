from django.shortcuts import render
from django.http import HttpResponse
import datetime
def timenow(request):
    t=datetime.datetime.now()
    return HttpResponse(t.strftime("%m"))
# Create your views here.
