import factory
from factory.django import DjangoModelFactory

from apps.posts.models import Post
from apps.users.factories import UserFactory


class PostFactory(DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    post = factory.Sequence(lambda x: f'Content of Title {x}')

    class Meta:
        model = Post