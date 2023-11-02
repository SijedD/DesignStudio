from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from .models import Applications, AdvUser
from django.views import generic


# Create your views here.


class ApplicationsView(generic.ListView):
    model = Applications
    template_name = 'index.html'
    context_object_name = 'application'


class RegistrateUser(CreateView):
    success_url = reverse_lazy('index')
    template_name = 'registration/register.html'
    form_class = RegisterUserForm


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'index.html'
