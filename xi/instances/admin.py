from django.contrib import admin

from xi.sitesx.admin import BaseAdmin
from xi.sitesx.admin import generate_list_display

from .models import Cluster
from .models import Instance


@admin.register(Instance)
class InstanceAdmin(BaseAdmin):
    """Instance admin"""

    list_display = generate_list_display(["site", "ip_address"])


@admin.register(Cluster)
class ClusterAdmin(BaseAdmin):
    """Cluster admin"""

    list_display = generate_list_display(["description"])
