from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from .models import KorisnickiProfil, FitnessCilj, Vjezba


# Kreiranje uloga
admin_group, created = Group.objects.get_or_create(name='Administrator')
user_group, created = Group.objects.get_or_create(name='Korisnik')

# Dodavanje permisija
permissions = Permission.objects.filter(content_type__app_label='main') 
admin_group.permissions.set(permissions)  # Administrator dobiva sve dozvole
user_group.permissions.set([])  # Korisnik nema posebne permisije

@admin.register(KorisnickiProfil)
class KorisnickiProfilAdmin(admin.ModelAdmin):
    list_display = ('korisnik', 'godine', 'visina', 'tezina')

@admin.register(FitnessCilj)
class FitnessCiljAdmin(admin.ModelAdmin):
    list_display = ('korisnik', 'naziv_cilja', 'ciljna_vrijednost', 'rok')

@admin.register(Vjezba)
class VjezbaAdmin(admin.ModelAdmin):
    list_display = ('korisnik', 'naziv_vjezbe', 'datum', 'trajanje')
# Register your models here.
