from django.contrib import admin
from .models import Work


class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'main_title',
        'sub_title_1',
        'main_title_2',
        'sub_title_2',
    )

admin.site.register(Work, WorkAdmin)
