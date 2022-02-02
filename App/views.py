from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def login_request(request):
    if request.method == "POST":
        formCategory = CategoryForm(request.POST)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('login_request')
    else:
        formCategory = CategoryForm()
    return render(request, "registration/login.html", {'formCategory': formCategory})

@login_required
def index(request):
    return render(request, "app/index.html")
