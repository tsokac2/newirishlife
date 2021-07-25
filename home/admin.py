from django.contrib import admin
from .models import Home


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'movie_quote',
        'p_1',
        'p_2',
        'p_3',
    )

admin.site.register(Home, HomeAdmin)
