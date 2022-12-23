from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def titleLoad(request):
    #pull data from db
    # transform data
    # send email
    return render(request, 'index.html')

def homeload(request):


    return render(request, 'homepage.html')

