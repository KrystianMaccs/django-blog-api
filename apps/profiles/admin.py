from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "ip_address",
         "country_code",
          "country_geoname_id",
           "longitude",
            "latitude",
             "joined_on_holiday",
              "ip_address"
              ]



admin.site.register(Profile, ProfileAdmin)
