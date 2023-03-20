from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from Character_Menagement.models import Character


# The character sheet view
class CharacterSheet(View):
    def get(self, request, id):
        character = Character.objects.get(id=id)
        if request.user.id != character.user_id:
            return HttpResponse("This isn't one of your characters")

        return render(request, 'character_sheet.html', {'character': character})


class CharacterEditing(View):
    def get(self, request, id):
        character = Character.objects.get(id=id)
        if request.user.id != character.user_id:
            return HttpResponse("This isn't one of your characters")

        return render(request, 'character_edit.html', {'character': character})

    def post(self, request, id):
        character = Character.objects.get(id=id)
        if request.user.id != character.user_id:
            return HttpResponse("This isn't one of your characters")

        character.clan = request.POST.get('clan')
        character.family = request.POST.get('family')
        character.name = request.POST.get('name')
        character.school = request.POST.get('school')
        character.notes = request.POST.get('notes')
        character.status = request.POST.get('status')
        character.glory = request.POST.get('glory')
        character.honor = request.POST.get('honor')
        character.ninjo = request.POST.get('ninjo')
        character.giri = request.POST.get('giri')
        character.air = request.POST.get('air')
        character.earth = request.POST.get('earth')
        character.fire = request.POST.get('fire')
        character.water = request.POST.get('water')
        character.void = request.POST.get('void')
        character.aesthetics = request.POST.get('aesthetics')
        character.composition = request.POST.get('composition')
        character.design = request.POST.get('design')
        character.smithing = request.POST.get('smithing')
        character.fitness = request.POST.get('fitness')
        character.meditation = request.POST.get('meditation')
        character.tactics = request.POST.get('tactics')
        character.melee = request.POST.get('melee')
        character.ranged = request.POST.get('ranged')
        character.unarmed = request.POST.get('unarmed')
        character.command = request.POST.get('command')
        character.courtesy = request.POST.get('courtesy')
        character.games = request.POST.get('games')
        character.performance = request.POST.get('performance')
        character.culture = request.POST.get('culture')
        character.government = request.POST.get('government')
        character.sentiment = request.POST.get('sentiment')
        character.theology = request.POST.get('theology')
        character.medicine = request.POST.get('medicine')
        character.commerce = request.POST.get('commerce')
        character.labour = request.POST.get('labour')
        character.seafaring = request.POST.get('seafaring')
        character.skullduggery = request.POST.get('skullduggery')
        character.survival = request.POST.get('survival')
        character.honor = request.POST.get('honor')

        character.save()

        return redirect(f'/account/character/{id}/')
