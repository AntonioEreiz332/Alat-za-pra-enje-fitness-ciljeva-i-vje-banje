from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, DetailView
from .models import *

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

class VjezbaListView(ListView):
    model = Vjezba
    template_name = 'vjezba_list.html'
    context_object_name = 'vjezbe'

    def get_queryset(self):

        #Filtriranje prema korisniku i pretraživanje prema nazivu vježbe.
        queryset = super().get_queryset()
        korisnik = self.request.GET.get('korisnik')  # Filtriranje prema korisniku
        search_query = self.request.GET.get('search')  # Pretraživanje prema nazivu vježbe

        if korisnik:
            queryset = queryset.filter(korisnik__korisnik__username=korisnik)
        if search_query:
            queryset = queryset.filter(naziv_vjezbe__icontains=search_query)

        return queryset

class FitnessCiljListView(ListView):
    model = FitnessCilj
    template_name = 'fitness_cilj_list.html'
    context_object_name = 'ciljevi'

    def get_queryset(self):
        
        #Filtriranje prema korisniku i pretraživanje prema nazivu cilja.
        queryset = super().get_queryset()
        korisnik = self.request.GET.get('korisnik')
        search_query = self.request.GET.get('search')

        if korisnik:
            queryset = queryset.filter(korisnik__korisnik__username=korisnik)
        if search_query:
            queryset = queryset.filter(naziv_cilja__icontains=search_query)

        return queryset
    
class KorisnickiProfilListView(ListView):
    model = KorisnickiProfil
    template_name = 'korisnickiprofil_list.html'
    context_object_name = 'profili'

    def get_queryset(self):

        #Pretraživanje profila prema korisničkom imenu.        
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(korisnik__username__icontains=search_query)
        return queryset

class VjezbaDetailView(DetailView):
    model = Vjezba
    template_name = 'vjezba_detail.html'
    context_object_name = 'vjezba'

class FitnessCiljDetailView(DetailView):
    model = FitnessCilj
    template_name = 'fitness_cilj_detail.html'
    context_object_name = 'cilj'

class KorisnickiProfilDetailView(DetailView):
    model = KorisnickiProfil
    template_name = 'korisnickiprofil_detail.html'
    context_object_name = 'profil'