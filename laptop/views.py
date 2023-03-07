from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_lap(request):
    return HttpResponse('this is the first function of laptop')
def second_lap(request):
    return HttpResponse('this is the second function of laptop')
