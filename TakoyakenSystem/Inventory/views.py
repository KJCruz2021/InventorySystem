from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#dito lalagay ung mga bagong page ng html

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def inventory(request):
    return render(request, 'inventory.html', {})

def customer(request):
    return render(request, 'customer.html', {})

def history(request):
    return render(request, 'history.html', {})
