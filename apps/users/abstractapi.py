import os

from blog_api.settings.base import env
from blog_api.settings import base
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators .cache import cache_page

import requests
import logging

logger = logging.getLogger("abstractapi")

CACHE_TTL = getattr(base, 'CACHE_TTL', DEFAULT_TIMEOUT)

class AbstractAPI(object):
    HOLIDAYS_API_KEY = env("HOLIDAYS_API_KEY")
    IP_GEOLOCATION_API_KEY = env("IP_GEOLOCATION_API_KEY")


    @cache_page(CACHE_TTL)
    def _get(self, url, max_tries=5, **params):
        tries = 0
        while tries < max_tries:
            tries += 1
            try:
                response = requests.get(url, params=params)
                if response.ok:
                    return response.json()
            except Exception as e:
                logger.error("Failed getting response(%s): %s", url, e)
        return None


    def get_holiday_details(self, country_code, year, month, day):
        url = "https://holidays.abstractapi.com/v1/"
        return self._get(
            url=url,
            day=day,
            year=year,
            month=month,
            country=country_code,
            api_key=self.HOLIDAYS_API_KEY,
        )

    def get_geolocation_details(self, ip_address):
        url = "https://ipgeolocation.abstractapi.com/v1/"
        return self._get(
            url=url,
            ip_address=ip_address,
            api_key=self.IP_GEOLOCATION_API_KEY,
        )
