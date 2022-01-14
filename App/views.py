from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "app\login.html")



def index(request):
    return render(request, "app\index.html")


    