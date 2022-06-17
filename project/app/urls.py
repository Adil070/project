from django.contrib import admin
from django.urls import path
from . import views
from .views import Login
from .views import Signup
from .views import Logout
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('register', Signup.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]
