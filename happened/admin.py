from django.contrib import admin
from .models import Event, Url


class UrlInline(admin.TabularInline):
    model = Url


admin.site.register(Event, inlines=[UrlInline])
admin.site.register(Url)
