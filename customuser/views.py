from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CreateUserForm
from .models import CreateUser
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class DashBoard(ListView):
    model = CreateUser
    template_name = 'dashboard.html'
    context_object_name = 'users'
    
class CreateUserView(CreateView):
    model = CreateUser
    form_class = CreateUserForm
    template_name = 'createuser.html'
    success_url = reverse_lazy('dashboard')