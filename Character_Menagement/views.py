from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from Character_Menagement.models import Character, Trait


# The character sheet view
class CharacterSheet(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect('/')

        character = Character.objects.get(id=id)
        if request.user.id != character.user_id:
            return HttpResponse("This isn't one of your characters")

        return render(request, 'character_sheet.html', {'character': character})


# The character editing view
class CharacterEditing(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect('/')

        character = Character.objects.get(id=id)
        # this line checks if the current user is the same as
        # the creator of the character
        if request.user.id != character.user_id:
            return HttpResponse("This isn't one of your characters")
        
        traits = Trait.objects.all()

        techniques = character.technique_categories.split(', ')

        print(techniques)

        return render(request, 'character_edit.html', {'character': character, 'techniques': techniques, 'traits': traits})

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

        character.traits.clear()

        traits = request.POST.getlist('traits')
        for element in traits:
            a = Trait.objects.get(name=element)
            character.traits.add(a)

        character.save()

        return redirect(f'/account/character/{id}/')


class CharacterCreation(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/')

        traits = Trait.objects.all()

        return render(request, 'character_create.html', {'traits': traits})

    def post(self, request):
        character = Character.objects.create(
            clan=request.POST.get('clan'),
            family=request.POST.get('family'),
            name=request.POST.get('name'),
            school=request.POST.get('school'),
            notes=request.POST.get('notes'),
            status=request.POST.get('status'),
            glory=request.POST.get('glory'),
            honor=request.POST.get('honor'),
            ninjo=request.POST.get('ninjo'),
            giri=request.POST.get('giri'),
            air=request.POST.get('air'),
            earth=request.POST.get('earth'),
            fire=request.POST.get('fire'),
            water=request.POST.get('water'),
            void=request.POST.get('void'),
            aesthetics=request.POST.get('aesthetics'),
            composition=request.POST.get('composition'),
            design=request.POST.get('design'),
            smithing=request.POST.get('smithing'),
            fitness=request.POST.get('fitness'),
            meditation=request.POST.get('meditation'),
            tactics=request.POST.get('tactics'),
            melee=request.POST.get('melee'),
            ranged=request.POST.get('ranged'),
            unarmed=request.POST.get('unarmed'),
            command=request.POST.get('command'),
            courtesy=request.POST.get('courtesy'),
            games=request.POST.get('games'),
            performance=request.POST.get('performance'),
            culture=request.POST.get('culture'),
            government=request.POST.get('government'),
            sentiment=request.POST.get('sentiment'),
            theology=request.POST.get('theology'),
            medicine=request.POST.get('medicine'),
            commerce=request.POST.get('commerce'),
            labour=request.POST.get('labour'),
            seafaring=request.POST.get('seafaring'),
            skullduggery=request.POST.get('skullduggery'),
            survival=request.POST.get('survival'),
            technique_categories='blank',
            user=request.user,
        )

        traits = request.POST.getlist('traits')
        for element in traits:
            a = Trait.objects.get(name=element)
            character.traits.add(a)

        technique_categories = request.POST.getlist('technique_categories')
        technique_categories_joined = ', '.join(technique_categories)
        character.technique_categories=technique_categories_joined
        character.save()

        return redirect('/account/')


class CharacterDelete(View):
    def get(self, request, id):
        character = Character.objects.get(id=id)
        if request.user.id != character.user_id:
            return HttpResponse("This isn't one of your characters")

        return render(request, 'character_delete.html', {'character': character})

    def post(self, request, id):
        character = Character.objects.get(id=id)
        if request.user.id != character.user_id:
            return HttpResponse("This isn't one of your characters")

        if 'no' in request.POST:
            return redirect(f'/account/character/{character.id}/')

        character.delete()

        return redirect('/account/')
