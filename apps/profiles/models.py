from django.db import models
from django.contrib.auth import get_user_model

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profiles", on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(protocol="both", blank=True, null=True)
    country_code = models.CharField(max_length=5, null=True, blank=True)
    country_geoname_id = models.IntegerField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    joined_on_holiday = models.BooleanField(default=False)

    class Meta:
        abstract = False