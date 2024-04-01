from django.contrib import admin

from xi.sitesx.admin import COMMON_FIELDS
from xi.sitesx.admin import BaseAdmin
from xi.sitesx.admin import generate_list_display

from .models import App
from .models import Version


@admin.register(App)
class AppAdmin(BaseAdmin):
    """App admin"""

    list_display = COMMON_FIELDS


@admin.register(Version)
class VersionAdmin(BaseAdmin):
    """Version admin"""

    list_display = generate_list_display(["app", "number", "is_approved"])
