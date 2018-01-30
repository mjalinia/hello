from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hi guys im joonline XD ")
