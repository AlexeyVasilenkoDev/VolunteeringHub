import os
import random
import string

import requests
from celery import shared_task
from django.contrib.auth import get_user_model
from faker import Faker

from volunteering.models import Category, Opportunity, Need, Accounting

fake = Faker()


def fetch_pic(subdir):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), f'media/{subdir}')
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{path}/{random_name}.jpg', 'wb') as f:
            f.write(response.content)
    return f"{subdir}/{random_name}.jpg"


@shared_task
def generate_user():
    get_user_model().objects.create(
        type=random.choice(["Single Volunteer", "Volunteers Organisation", "Civil Person", "Military Person"]),
        username=fake.word(),
        email=fake.ascii_safe_email(),
        phone=fake.phone_number(),
    )


@shared_task
def generate_category():
    Category.objects.create(name=fake.word().capitalize())


@shared_task
def generate_accounting():
    Accounting.objects.create(photo=fetch_pic("accounting"), description=fake.sentence(nb_words=10))


@shared_task
def generate_opportunity():
    opp = Opportunity(
        title=fake.word().capitalize(),
        description=fake.sentence(nb_words=10),
        photo=fetch_pic("opportunity"),
        city=fake.location_on_land()[2],
        author=random.choice(get_user_model().objects.all())
    )
    opp.save()
    opp.category.set(
        random.choices([i[0] for i in list(Category.objects.values_list('id'))], k=random.choice(range(1, 5))))


@shared_task
def generate_need():
    need = Need(
        title=fake.word().capitalize(),
        description=fake.sentence(nb_words=10),
        price=fake.random_int(min=0, max=1_000_000_000),
        donation=f"https://{fake.domain_name()}",
        accounting=random.choice(Accounting.objects.all()),
        photo=fetch_pic("need"),
        city=fake.location_on_land()[2],
        is_satisfied=random.choice([True, False])
    )
    need.save()
    need.category.set(
        random.choices([i[0] for i in list(Category.objects.values_list('id'))], k=random.choice(range(1, 5))))
    need.author.set(random.choices(list(get_user_model().objects.all())))
