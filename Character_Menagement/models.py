from django.db import models

from Account_management.models import User

# This is for Traits
TRAIT_TYPES = (
    ('1', 'Curse'),
    ('2', 'Flaw'),
    ('3', 'Interpersonal'),
    ('4', 'Infamy'),
    ('5', 'Mental'),
    ('6', 'Physical'),
    ('7', 'Scar'),
    ('8', 'Spiritual'),
    ('9', 'Virtue'),
)


TRAIT_CATEGORY = (
    ('1', 'Distinction'),
    ('2', 'Adversity'),
    ('3', 'Passion'),
    ('4', 'Anxiety'),
)


# This is the model for Distinctions, Adversities, Anxieties and Passions
class Trait(models.Model):
    name = models.CharField(max_length=64, unique=True)
    ring = models.CharField(max_length=5)
    category = models.CharField(
        max_length=24,
        choices=TRAIT_CATEGORY,
    )
    type1 = models.CharField(
        max_length=24,
        choices=TRAIT_TYPES,
    )
    type2 = models.CharField(
        max_length=24,
        choices=TRAIT_TYPES,
        null=True,
    )
    type3 = models.CharField(
        max_length=24,
        choices=TRAIT_TYPES,
        null=True,
    )


# These are the models for Item Qualities and equipment including armor and weapons
# price is given in Zeni (1 koku = 5 bu = 50 zeni)
class ItemQuality(models.Model):
    name = models.CharField(max_length=24, unique=True)
    description = models.TextField(null=True)
    effect = models.TextField(null=True)
    opportunities = models.TextField(null=True)


class Equipment(models.Model):
    name = models.CharField(max_length=64, unique=True)
    rarity = models.IntegerField()
    price = models.IntegerField()
    qualities = models.ManyToManyField(ItemQuality)
    description = models.TextField(null=True)


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


class Armor(models.Model):
    name = models.CharField(max_length=64, unique=True)
    rarity = models.IntegerField()
    price = models.IntegerField()
    qualities = models.ManyToManyField(ItemQuality)
    description = models.TextField(null=True)
    physical_reduction = models.IntegerField(default=0)
    supernatural_reduction = models.IntegerField(default=0)


# This is the model for techniques
class Technique(models.Model):
    name = models.CharField(max_length=64, unique=True)
    category = models.CharField(max_length=24)
    rings = models.CharField(max_length=24, null=True)
    action_types = models.CharField(max_length=64, null=True)
    rank = models.IntegerField()
    prerequisites = models.CharField(max_length=36)
    description = models.TextField()
    xp_cost = models.IntegerField(default=30)
    activation = models.TextField()
    effect = models.TextField(null=True)
    opportunities = models.TextField(null=True)


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


# This is the Character model
class Character(models.Model):
    # Clan, Family, name and school
    clan = models.CharField(max_length=24)
    family = models.CharField(max_length=24)
    name = models.CharField(max_length=24)
    school = models.CharField(max_length=64)
    notes = models.TextField(null=True)

    # social atributes, ninjo and giri
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
    traits = models.ManyToManyField(Trait)

    # Equipment
    weapons = models.ManyToManyField(Weapon)
    armour = models.ManyToManyField(Armor)
    equipment = models.ManyToManyField(Equipment)

    # Abilities
    technique_categories = models.CharField(max_length=64)
    techniques = models.ManyToManyField(Technique)
    school_ability = models.ManyToManyField(SchoolAbility)

    # Meta information
    date_of_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
