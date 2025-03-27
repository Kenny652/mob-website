from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('home')

        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('Password Or Email Address Incorrect'))
            print('you fucked up')
            return redirect('login/')
        
    
    else :
        return render(request, 'registration/login.html', {})