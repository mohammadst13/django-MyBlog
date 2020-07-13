from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    forms = UserCreationForm()
    return render(request, 'accounts/signup.html', {'forms' : forms})
