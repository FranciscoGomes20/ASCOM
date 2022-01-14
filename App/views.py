from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Você está logado agora {username}.")
                return redirect("index")
            else:
                messages.error(request, "Username or password is invalid.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "registration/login.html", {'form':form})

@login_required
def index(request):
    return render(request, "app/index.html")

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    redirect('login_request')