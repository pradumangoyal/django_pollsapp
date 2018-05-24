from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
# Create your views here.

def signup(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passkey = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_passkey)
            login(request, user)
            return redirect('../../polls')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


