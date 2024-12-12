from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

def home(request):
    return render(request, 'home.html')  

# Funkcija koja provjerava je li korisnik administrator
def is_admin(user):
    return user.groups.filter(name='Administrator').exists()

# Dashboard za administratore
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

# Dashboard za obične korisnike
@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')

