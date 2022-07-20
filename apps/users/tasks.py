from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model

from celery import shared_task
from apps.users.abstractapi import AbstractAPI

User = get_user_model()

@shared_task
def enrich_user(user_pk):
    user = User.objects.get(pk=user_pk)
    api = AbstractAPI()

    location_details = api.get_geolocation_details(ip_address=user.ip_address)
    if location_details is not None:
        user.country = location_details.get("country")
        user.country_code = location_details.get("country_code")
        user.country_geoname_id = location_details.details.get("country_geoname_id")
        user.longitude = location_details.get("longitude")
        user.latitude = location_details.get("latitude")
        user.save(update_fields=("country", "country_code", "country_geoname_id", "longitude", "latitude"))

    holiday_details = api.get_holiday_details(
        country_code=user.country_code,
        day=user.date_joined.day,
        month=user.date_joined.month,
        year=user.date_joined.year,
    )

    if holiday_details is not None and any(holiday_details):
        user.joined_on_holiday = True
        user.save(update_fields=("joined_on_holiday",))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.joined_on_holiday == False:
        instance.joined_on_holiday = True
        instance.save()