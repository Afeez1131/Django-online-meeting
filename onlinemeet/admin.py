from django.contrib import admin
from .models import Meeting


class CustomAdmin(admin.ModelAdmin):
    list_display = ["creator", "title_of_meeting", "created", "updated"]

admin.site.register(Meeting, CustomAdmin)