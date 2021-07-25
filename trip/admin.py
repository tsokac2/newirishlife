from django.contrib import admin
from .models import Trip


class TripAdmin(admin.ModelAdmin):
    list_display = (
        'main_title',
        'sub_title_1',
        'sub_title_2',
        'sub_title_3',
    )

admin.site.register(Trip, TripAdmin)