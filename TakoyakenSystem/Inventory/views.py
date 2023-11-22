from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.

#dito lalagay ung mga bagong page ng html


def signup(request):

    if request.method == "POST":
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(email,pass1)
        myuser.email = email
        myuser.password = pass1
        myuser.save()

        return redirect('signup')
    return render(request, 'signup.html', {})

def login(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']

        user = authenticate(email=email, password=pass1)

        if user is not None:
            login(request,user)
            email = user.email
            return render(request, 'inventory')
        
        else:
            messages.erro(request, "Wrong Info")
            return redirect('login.html')

    return render(request, 'login.html', {})


def inventory(request):
    return render(request, 'inventory.html', {})

def customer(request):
    return render(request, 'customer.html', {})

def history(request):
    return render(request, 'history.html', {})
