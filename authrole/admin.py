from django.contrib import admin

from .models import Role


# @admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('name',)
    filter_horizontal = ('groups',)

admin.site.register(Role, RoleAdmin)
