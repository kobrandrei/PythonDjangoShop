from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserOurRegistration
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserOurRegistration(request.POST);
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registration.html', {'form': form})

