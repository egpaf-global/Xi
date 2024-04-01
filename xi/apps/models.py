from django.db import models
from django.utils.translation import gettext_lazy as _

from xi.sitesx.models import BaseModel


class Version(BaseModel):
    """App version"""

    name = models.CharField(_("name"), max_length=64)
    number = models.CharField(
        _("number"),
        max_length=64,
        help_text=_("Version number of the App. Usually formatted as v1.0"),
    )
    is_approved = models.BooleanField(_("Version approved?"), default=False)

    def __str__(self) -> str:
        return str(self.number)


class App(BaseModel):
    """App/system"""

    name = models.CharField(_("name"), max_length=64)
    description = models.TextField(blank=True)
    repo_url = models.CharField(_("repo URL"), max_length=300)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.number)
