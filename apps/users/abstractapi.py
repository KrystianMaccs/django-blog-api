import os

import requests

class AbstractAPI(object):
    HOLIDAYS_API_KEY = os.environ.get("HOLIDAYS_API_KEY")
    IP_GEOLOCATION_API_KEY = os.environ.get("IP_GEOLOCATION_API_KEY")


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
