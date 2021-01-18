from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login

from pathlib import Path
import os, sys


def MainPage(request):
    return render(request, 'main_page.html', context={})


class BaumandaysLoginView(LoginView):
    template_name = 'Login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('MainPage')
    def get_success_url(self):
        return self.success_url


class BaumandaysRegisterView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'Register.html'
    success_url = reverse_lazy('MainPage')
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username = username, password = password)
        login(self.request, aut_user)
        return form_valid



class BaumandaysLogoutView(LogoutView):
    next_page = reverse_lazy('MainPage')