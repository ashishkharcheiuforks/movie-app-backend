from django.contrib import admin

from .models import Parameter


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'description', 'admin_list_value', 'updated_at')
    readonly_fields = ('key', 'description')
    search_fields = ('key', 'description', 'value')
    fieldsets = (
        (None, {'fields': ('key', 'description', 'value')}),
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
