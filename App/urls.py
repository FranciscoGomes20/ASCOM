from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_request, name='login'),
    path('', views.index, name='index'),
]