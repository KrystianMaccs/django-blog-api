from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedUUIDModel
from apps.posts.models import Post
from blog_api.settings.base import AUTH_USER_MODEL

class Like(TimeStampedUUIDModel):
    post = models.OneToOneField(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ManyToManyField(AUTH_USER_MODEL, related_name="requirement_post_likes")

    def __str__(self):
        return str(self.post.post)[:30]

class UnLike(TimeStampedUUIDModel):
    post = models.OneToOneField(Post, related_name="un_likes", on_delete=models.CASCADE)
    user = models.ManyToManyField(AUTH_USER_MODEL, related_name="requirement_post_un_likes")

    def __str__(self):
        return str(self.post.post)[:30]