from faker import Faker
from django.contrib.auth import get_user_model
import factory
from factory.django import DjangoModelFactory

User = get_user_model()
fake = Faker()


class UserFactory(DjangoModelFactory):
    first_name = fake.first_name
    last_name = fake.last_name
    email = fake.email

    class Meta:
        model = User