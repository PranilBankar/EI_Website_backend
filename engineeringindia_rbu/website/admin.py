# website/admin.py
from django.contrib import admin
from .models import Member, Project, Event  # optional if you create models

admin.site.register(Member)
admin.site.register(Project)
admin.site.register(Event)
