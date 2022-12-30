from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

def loginLoad(request):
    #pull data from db
    # transform data
    # send email
    logout(request)
    username = password = ''
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
    else:
        return render(request, 'login.html')

def personalLoad(request):


    return render(request, 'personal.html')


def BShomeLoad(request):

    return render(request, 'BSHome.html')

