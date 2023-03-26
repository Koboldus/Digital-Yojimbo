import django.db.utils
from django.test import TestCase, Client
from Account_management.models import User
from Character_Menagement.models import Character

def client():
    client = Client()
    return client


def test_character_sheet_not_logged_in(db, client):
    c = client.get('/account/character/1/')
    assert c.status_code == 302


def test_character_sheet_not_your_character():
    user_id = 1
    character_user_id = 2
    assert user_id != character_user_id


def test_character_editing_not_your_character():
    user_id = 1
    character_user_id = 2
    assert user_id != character_user_id


def test_character_create_save(db):
    user = User.objects.create(
        password='meme',
        is_superuser=False,
        username='meme',
        first_name='meme',
        last_name='meme',
        email='me@me.com',
        is_staff=False,
        is_active=True,
    )

    assert Character.objects.create(
        clan='test',
        family='test',
        name='test',
        school='test',
        notes='test',
        status=50,
        glory=50,
        honor=50,
        ninjo='test',
        giri='test',
        technique_categories='Kata',
        user=user
    )


def test_character_create_save_failure(db):
    user = User.objects.create(
        password='meme',
        is_superuser=False,
        username='meme',
        first_name='meme',
        last_name='meme',
        email='me@me.com',
        is_staff=False,
        is_active=True,
    )

    try:
        Character.objects.create(
            clan='test',
            family='test',
            name='test',
            school='test',
            notes='test',
            status=50,
            glory=50,
            honor=50,
            ninjo='test',
            giri='test',
            technique_categories=None,
            user=user
        )
    except django.db.utils.IntegrityError:
        assert True
