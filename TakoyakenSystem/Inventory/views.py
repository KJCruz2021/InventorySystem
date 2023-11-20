from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#dito lalagay ung mga bagong page ng html

def login(request):
    return render(request, 'login.html', {})
