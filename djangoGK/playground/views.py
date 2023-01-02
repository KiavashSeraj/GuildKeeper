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

    user_name = request.user.get_full_name()
    context = {'user_name': user_name}

    return render(request, 'personal.html', context)

@login_required
def BShomeLoad(request):

    return render(request, 'BSHome.html')

