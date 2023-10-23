from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():  
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        
    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            return reverse('accounts:login')
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)