from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id", "pkid", "username", "first_name", "last_name", "country"]
    list_display_links = ["id", "pkid", "username"]



admin.site.register(User, UserAdmin)
