from faker import Faker
from django.contrib.auth import get_user_model
#from factory import fuzzy
from factory.django import DjangoModelFactory

User = get_user_model()
fake = Faker()


class UserFactory(DjangoModelFactory):
    first_name = fake.first_name
    """last_name = fuzzy.FuzzyAttribute(fuzzer=fake.last_name)
    email = fuzzy.FuzzyAttribute(fuzzer=fake.email)"""

    class Meta:
        model = User