from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('register/', RegistrateUser.as_view(), name='register'),
    path('', views.ApplicationsView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login')
]
