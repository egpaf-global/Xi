from django.contrib import admin

from .models import District
from .models import Site
from .models import Zone

COMMON_FIELDS = [
    "name",
    "created_by",
    "created_at",
]


def generate_list_display(additional_fields):
    return COMMON_FIELDS + additional_fields


class BaseAdmin(admin.ModelAdmin):
    """
    Base admin class providing common functionality.
    Excludes 'created_at' and 'created_by' fields from the form.
    """

    def get_exclude(self, request, obj=None):
        exclude = super().get_exclude(request, obj)
        return (
            (*exclude, "created_at", "created_by")
            if exclude
            else ("created_at", "created_by")
        )

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # if it's a new object
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Zone)
class ZoneAdmin(BaseAdmin):
    """Zone admin"""

    list_display = generate_list_display(["contact"])


@admin.register(District)
class DistrictAdmin(BaseAdmin):
    """District admin"""

    list_display = generate_list_display(["contact"])


@admin.register(Site)
class SiteAdmin(BaseAdmin):
    """Site admin"""

    list_display = generate_list_display(["district"])
