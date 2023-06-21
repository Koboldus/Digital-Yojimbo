from django.db import models

from Account_management.models import User


# This is the model for Distinctions, Adversities, Anxieties and Passions
class Trait(models.Model):
    name = models.CharField(max_length=64, unique=True)
    ring = models.CharField(max_length=5)
    category = models.CharField(max_length=24)
    type1 = models.CharField(max_length=24)
    type2 = models.CharField(
        max_length=24,
        null=True
    )
    type3 = models.CharField(
        max_length=24,
        null=True
    )

    def __str__(self):
        return self.name


# These are the models for Item Qualities and equipment including armor and weapons
# price is given in Zeni (1 koku = 5 bu = 50 zeni)
class ItemQuality(models.Model):
    name = models.CharField(max_length=24, unique=True)
    description = models.TextField(null=True)
    effect = models.TextField(null=True)
    opportunities = models.TextField(null=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=64, unique=True)
    rarity = models.IntegerField()
    price = models.IntegerField()
    qualities = models.ManyToManyField(ItemQuality)
    description = models.TextField(null=True)
    abilities = models.TextField(null=True)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=64, unique=True)
    rarity = models.IntegerField()
    price = models.IntegerField()
    qualities = models.ManyToManyField(ItemQuality)
    description = models.TextField(null=True)
    skill = models.CharField(max_length=12)
    range = models.CharField(max_length=3)
    damage = models.IntegerField()
    deadliness = models.IntegerField()
    one_hand = models.CharField(max_length=24, null=True)
    two_hand = models.CharField(max_length=24, null=True)
    quirks = models.CharField(max_length=240, null=True)
    type = models.CharField(max_length=30, default='sword')

    def __str__(self):
        return self.name


class Armor(models.Model):
    name = models.CharField(max_length=64, unique=True)
    rarity = models.IntegerField()
    price = models.IntegerField()
    qualities = models.ManyToManyField(ItemQuality)
    description = models.TextField(null=True)
    physical_resistance = models.IntegerField(default=0)
    supernatural_resistance = models.IntegerField(default=0)
    quirks = models.CharField(max_length=240, null=True)

    def __str__(self):
        return self.name


# This is the model for techniques
class Technique(models.Model):
    name = models.CharField(max_length=64, unique=True)
    category = models.CharField(max_length=24)
    air = models.BooleanField(default=False)
    earth = models.BooleanField(default=False)
    fire = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    void = models.BooleanField(default=False)
    attack = models.BooleanField(default=False)
    movement = models.BooleanField(default=False)
    scheme = models.BooleanField(default=False)
    support = models.BooleanField(default=False)
    rank = models.IntegerField()
    prerequisites = models.CharField(max_length=36)
    description = models.TextField()
    xp_cost = models.IntegerField(default=30)
    activation = models.TextField()
    effect = models.TextField(null=True)
    burst = models.TextField(null=True)
    opportunities = models.TextField(null=True)

    def __str__(self):
        return self.name


# This is the model for school and mastery abilities
# The 'is_mastery_ability' defines if it's a school (False) or mastery (True) ability
class SchoolAbility(models.Model):
    name = models.CharField(max_length=64, unique=True)
    is_mastery_ability = models.BooleanField(default=False)
    rings = models.CharField(max_length=24, null=True)
    action_types = models.CharField(max_length=64, null=True)
    description = models.TextField(null=True)
    activation = models.TextField(null=True)
    effect = models.TextField(null=True)
    opportunities = models.TextField(null=True)

    def __str__(self):
        return self.name


# This is the Character model
class Character(models.Model):
    # Clan, Family, name and school
    clan = models.CharField(max_length=24)
    family = models.CharField(max_length=24)
    name = models.CharField(max_length=24)
    school = models.CharField(max_length=64)
    notes = models.TextField(null=True)

    # social attributes, ninjo and giri
    status = models.IntegerField()
    glory = models.IntegerField()
    honor = models.IntegerField()
    ninjo = models.CharField(max_length=240)
    giri = models.CharField(max_length=240)

    # Rings
    air = models.IntegerField(default=1)
    earth = models.IntegerField(default=1)
    fire = models.IntegerField(default=1)
    water = models.IntegerField(default=1)
    void = models.IntegerField(default=1)

    # Skill groups
    # Artisan Skills
    aesthetics = models.IntegerField(default=0)
    composition = models.IntegerField(default=0)
    design = models.IntegerField(default=0)
    smithing = models.IntegerField(default=0)

    # Martial Skills
    fitness = models.IntegerField(default=0)
    meditation = models.IntegerField(default=0)
    tactics = models.IntegerField(default=0)
    melee = models.IntegerField(default=0)
    ranged = models.IntegerField(default=0)
    unarmed = models.IntegerField(default=0)

    # Social Skills
    command = models.IntegerField(default=0)
    courtesy = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)

    # Scholar Skills
    culture = models.IntegerField(default=0)
    government = models.IntegerField(default=0)
    sentiment = models.IntegerField(default=0)
    theology = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)

    # Trade Skills
    commerce = models.IntegerField(default=0)
    labour = models.IntegerField(default=0)
    seafaring = models.IntegerField(default=0)
    skullduggery = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)

    # Traits
    traits = models.ManyToManyField(Trait, related_name='trait')

    # Equipment
    weapons = models.ManyToManyField(Weapon, related_name='weapon')
    armor = models.ManyToManyField(Armor, related_name='defense')
    equipment = models.ManyToManyField(Equipment, related_name='eq')

    # Abilities
    technique_categories = models.CharField(max_length=64)
    techniques = models.ManyToManyField(Technique, related_name='techs')
    school_ability = models.ManyToManyField(SchoolAbility, related_name='school_abi')

    # Meta information
    date_of_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    