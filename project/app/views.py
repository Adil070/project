from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Index(View):
    # @login_required(login_url='login')
    def get(self, request):
        return render(request, "home.html")


class Signup(View):
    def get(self, request):
        request.user.is_authenticated
        return redirect('home')

    def post(self, request):
        form = CreateUserForm()
        context = {'form': form}

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        return render(request, 'register.html', context)


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'login.html')

    def post(self, request):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "invalid credentials")

        return render(request, 'login.html')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
