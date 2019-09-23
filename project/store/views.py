from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    return HttpResponse('Привет, вы на главной странице сайта Django store')
