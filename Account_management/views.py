from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class Main(View):
    def get(self, request):
        return render(request, 'main_login.html')

    def post(self, request):
        return render(request, 'main_logged_in.html')