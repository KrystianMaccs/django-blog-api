from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedUUIDModel
#from apps.reactions.models import Like, UnLike
from blog_api.settings.base import AUTH_USER_MODEL



class Post(TimeStampedUUIDModel):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name=_("posts"), on_delete=models.CASCADE)
    post = models.TextField(blank=False, null=False)

    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_unlikes(self):
        return self.unlikes.users.count()

    def __str__(self):
        return str(self.comment)[:30]