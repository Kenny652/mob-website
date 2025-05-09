from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here

def login_user(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home-page')
            # Redirect to a success page.
        else:
            messages.success(request, ('Mot de passe incorrect.'))
            return render(request, 'authenticate/login.html', {})

        
        # Return an 'invalid login' error message.

    else:
        return render(request, 'authenticate/login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ('Vous avez été déconnecté'))
    return redirect('home:home-page')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Vous avez été authentifié')
            return redirect('home:home-page')
    else :
        form = RegisterUserForm()
            
    return render(request, 'authenticate/register.html', {
        'form':form,
    })






