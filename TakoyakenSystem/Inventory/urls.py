from django.contrib import admin
from django.urls import path
from . import views

#dito ung parang paths / url nila
#nakaconnect to sa views.py (kung ano mga function don, dapat nakalagay din dto)

urlpatterns = [
    path('', views.login, name='login'),  
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('inventory/', views.inventory, name='inventory'),
    path('customer/', views.customer, name='customer'),
    path('history/', views.history, name='customer')
]