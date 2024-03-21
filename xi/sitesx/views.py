from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView

from xi.sitesx import models


class CreateSiteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    # required perm for the view
    permission_required: str = "sitesx.add_site"

    model = models.Site
    success_message = _("New site added successfully")
    fields = ["name", "district"]


create_site_view = CreateSiteView.as_view()
