"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Character_Menagement.views import (
    CharacterSheet,
    CharacterEditing,
    CharacterCreation,
    CharacterDelete,
)
from Account_management.views import (
    Main,
    Register,
    LoggedInView,
    AccountDelete,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view()),
    path('register/', Register.as_view()),
    path('account/', LoggedInView.as_view()),
    path('account/delete/', AccountDelete.as_view()),
    path('account/character/create/', CharacterCreation.as_view()),
    path('account/character/<id>/', CharacterSheet.as_view()),
    path('account/character/<id>/edit/', CharacterEditing.as_view()),
    path('account/character/<id>/delete/', CharacterDelete.as_view()),
]
