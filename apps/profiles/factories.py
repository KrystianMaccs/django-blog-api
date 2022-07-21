from faker import Faker
from django.contrib.auth import get_user_model
from apps.profiles.models import Profile
from factory import fuzzy
from factory.django import DjangoModelFactory

User = get_user_model()
fake = Faker()


class ProfileFactory(DjangoModelFactory):
    ip_address = fuzzy.FuzzyAttribute(fuzzer=fake.ip_address)
    joined_on_holiday = fuzzy.FuzzyAttribute(fuzzer=fake.last_name)

    class Meta:
        model = Profile