from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from Account_management.models import User
from Character_Menagement.models import Character


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

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=mail,
            username=username,
            password=password,
        )

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/account/')


class LoggedInView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/')

        username = request.user.username

        characters = Character.objects.filter(user_id=request.user.id)

        return render(request, 'main_logged_in.html', {'username': username, 'characters': characters})

    def post(self, request):
        logout(request)
        return redirect('/')


class AccountDelete(View):
    def get(self, request, retry=0):
        if not request.user.is_authenticated:
            return redirect('/')

        return render(request, 'delete_account.html', {'retry': retry})

    def post(self, request):
        username = request.POST.get('username')
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        user = authenticate(username=username, email=mail, password=password)
        if user is not None and username == request.user.username:
            to_delete = User.objects.get(username=username)
            to_delete.delete()
            return redirect('/')

        return render(request, 'delete_account.html', {'retry': 1})
