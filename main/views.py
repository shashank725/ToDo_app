from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hi</h1>')