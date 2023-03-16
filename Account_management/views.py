from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from Account_management.models import L5RUser


# Create your views here.
class Main(View):
    def get(self, request, retry=0):
        if request.user.is_authenticated:
            return redirect('/account/')
        return render(request, 'main_login.html', {'retry': retry})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/account/')

        return render(request, 'main_login.html', {'retry': 1})


class Register(View):
    def get(self, request, retry=0):
        return render(request, 'registration.html', {'retry': retry})

    def post(self, request):
        if request.POST.get('password') != request.POST.get('password_repeat'):
            return render(request, 'registration.html', {'retry': 1})

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mail = request.POST.get('mail')
        username = request.POST.get('username')
        password = request.POST.get('password')

        L5RUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=mail,
            username=username,
            password=password,
        )

        return HttpResponse('Created Account')


class LoggedInView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/')

        username = request.user.username

        return render(request, 'main_logged_in.html', {'username': username})

    def post(self, request):
        logout(request)
        return redirect('/')
