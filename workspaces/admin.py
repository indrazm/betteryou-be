from django.contrib import admin
from .models import Workspace, Space


# Register your models here.
@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at", "updated_at"]


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "workspace", "created_at", "updated_at"]
