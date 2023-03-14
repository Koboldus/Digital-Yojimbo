from django.db import models


# This is for traits
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


# This is the model for Distinctions, Adversities, Anxieties and Passions
class Trait(models):
    name = models.CharField(max_length=64)
    ring = models.CharField(max_length=5)
    type1 = models.CharField(
        max_length=1,
        choices=TRAIT_TYPES,
    )
    type2 = models.CharField(
        max_length=1,
        choices=TRAIT_TYPES,
        null=True,
    )
    type3 = models.CharField(
        max_length=1,
        choices=TRAIT_TYPES,
        null=True,
    )


# These are the models for Item Qualities and equipment including armor and weapons
# price is given in Zeni (1 koku = 5 bu = 50 zeni)
class ItemQuality(models):
    name = models.CharField(24)
    description = models.TextField()
    opportunities = models.TextField()


class Equipment(models):
    name = models.CharField(max_length=64)
    rarity = models.IntegerField()
    price = models.IntegerField()
    quality1 = models.ManyToManyField(ItemQuality, null=True)
    quality2 = models.ManyToManyField(ItemQuality, null=True)
    quality3 = models.ManyToManyField(ItemQuality, null=True)
    description = models.TextField(null=True)


class Weapon(models):
    name = models.CharField(max_length=64)
    rarity = models.IntegerField()
    price = models.IntegerField()
    quality1 = models.ManyToManyField(ItemQuality, null=True)
    quality2 = models.ManyToManyField(ItemQuality, null=True)
    quality3 = models.ManyToManyField(ItemQuality, null=True)
    description = models.TextField(null=True)
    skill = models.CharField()
    range = models.CharField(max_length=3)
    damage = models.IntegerField()
    deadliness = models.IntegerField()
    one_hand = models.CharField(24, null=True)
    two_hand = models.CharField(24, null=True)


class Armor(models):
    name = models.CharField(max_length=64)
    rarity = models.IntegerField()
    price = models.IntegerField()
    quality1 = models.ManyToManyField(ItemQuality, null=True)
    quality2 = models.ManyToManyField(ItemQuality, null=True)
    quality3 = models.ManyToManyField(ItemQuality, null=True)
    description = models.TextField(null=True)
    physical_reduction = models.IntegerField(default=0)
    supernatural_reduction = models.IntegerField(default=0)


# This is the Character model
class Character(models):
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
    ninjo = models.TextField()
    giri = models.TextField()

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
    distinctions = models.ManyToManyField(Trait)
    adversities = models.ManyToManyField(Trait)
    passions = models.ManyToManyField(Trait)
    anxieties = models.ManyToManyField(Trait)

    # Equipment
    weapons = models.ManyToManyField(Weapon, null=True)
    armour = models.ManyToManyField(Armor, null=True)
    equipment = models.ManyToManyField(Equipment, null=True)
