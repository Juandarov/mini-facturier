from django.contrib import admin
from models import Project, ProjectLine, Status, Client

# Register your models here.

class ProjectInLine(admin.TabularInline):
    model = ProjectLine

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectInLine, ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Status)
admin.site.register(Client)
