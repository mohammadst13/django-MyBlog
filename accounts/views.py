from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signup_view(request):
    if request.method == "POST":
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            user = forms.save()

            login(request, user)

            # login

            return redirect('articles:list')
    else:
        forms = UserCreationForm()
    return render(request, 'accounts/signup.html', {'forms' : forms})

def login_view(request):
    if request.method == "POST":
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            # login User
            user = forms.get_user()

            login(request, user)

            return redirect('articles:list')
    else:
        forms = AuthenticationForm()
        return render(request, 'accounts/login.html', {'forms' : forms})

def logout_view(request):
    if request.method == "POST":
        logout(request)

    return redirect('articles:list')
