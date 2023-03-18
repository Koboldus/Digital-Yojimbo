from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from Character_Menagement.models import Character

# The character sheet view
class CharacterSheet(View):
    def get(self, request, id):
        character = Character.objects.get(id=id)
        if request.user.id != character.user_id:
            return HttpResponse("You can't look at other people's characters")

        return render(request, 'character_sheet.html', {'character': character})
