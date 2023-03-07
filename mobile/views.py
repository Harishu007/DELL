from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_mobile(request):
    return HttpResponse('this is the first function of mobile')
def second_mobile(request):
    return HttpResponse('this is the SECOND function of mobile')

