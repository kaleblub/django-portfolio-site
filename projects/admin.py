from django.contrib import admin
from .models import Language, Project

admin.site.register(Project)
admin.site.register(Language)