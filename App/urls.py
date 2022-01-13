from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('index', views.index, name='index'),
]