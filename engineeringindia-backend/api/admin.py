# api/admin.py
from django.contrib import admin
from .models import Event, Registration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "start_time", "location", "capacity", "created_by")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description", "location")

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("event", "user", "registered_at")
    search_fields = ("user__email", "event__title")
