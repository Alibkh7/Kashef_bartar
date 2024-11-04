from django.contrib import admin
from .models import Contact, Team


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'meli_code', 'email', 'phone', 'message')
    search_fields = ('meli_code',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'career', 'image', 'text')
    search_fields = ('name',)
