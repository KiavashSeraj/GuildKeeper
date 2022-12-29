from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loginLoad(request):
    #pull data from db
    # transform data
    # send email
    return render(request, 'login.html')

def personalLoad(request):

    return render(request, 'personal.html')


def BShomeLoad(request):


    return render(request, 'BSHome.html')

