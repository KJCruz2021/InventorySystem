from django.urls import path
from . import views

#dito ung parang paths / url nila
#nakaconnect to sa views.py (kung ano mga function don, dapat nakalagay din dto)

urlpatterns = {
    path('', views.login, name="login"),
    path('signup/', views.signup, name='signup')
}