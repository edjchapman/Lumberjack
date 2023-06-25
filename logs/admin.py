from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from logs.models import ExceptionLog


def mark_resolved(cls, request, queryset):
    """
    Admin action, allows batch setting logs to resolved.
    """
    queryset.update(resolved=True)


@admin.register(ExceptionLog)
class ExceptionLogAdmin(admin.ModelAdmin):
    fields = [
        'project_name',
        'appenv',
        'app_location',
        'created_at',
        'level',
        'subject',
        'logger_name',
        'path_name',
        'func_name',
        'line_num',
        'traceback',
        'resolved',
    ]
    readonly_fields = [
        'project_name',
        'appenv',
        'app_location',
        'created_at',
        'level',
        'subject',
        'logger_name',
        'path_name',
        'func_name',
        'line_num',
        'traceback',
    ]
    list_display = [
        'project_name',
        'appenv',
        'app_location',
        'created_at',
        'subject',
        'resolved',
    ]
    list_editable = [
        "resolved"
    ]
    list_filter = (
        'project_name',
        'appenv',
        'app_location',
        'resolved',
        ('created_at', DateRangeFilter),
        'logger_name',
    )
    search_fields = [
        'subject',
        'logger_name',
        'path_name',
        'func_name',
    ]
    actions = [mark_resolved]

    def has_delete_permission(self, request, obj=None):
        """
        Disables delete permissions for non super-users.
        """
        if request.user.is_superuser:
            return True

    def has_add_permission(self, request):
        """
        Disabling the create permissions
        """
        return False
