from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

@login_required
def personalLoad(request):


    return render(request, 'personal.html')

@login_required
def BShomeLoad(request):

    return render(request, 'BSHome.html')

