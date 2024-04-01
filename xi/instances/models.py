from django.db import models
from django.utils.translation import gettext_lazy as _

from xi.sitesx.models import BaseModel
from xi.sitesx.models import Site


class Instance(BaseModel):
    """
    Represents a virtual or metal host instance.

    Attributes:
        name (str): The name of the instance.
        description (str, optional): Description of the instance.
        site (Site): The site to which the instance belongs, referenced by foreign key.
        ip_address (str): IPv4 address of the instance.
        username (str): Username for SSH access to the instance.

    Methods:
        __str__(): Returns the name of the instance as a string.
    """

    name = models.CharField(_("name"), max_length=64)
    description = models.TextField(_("description"), blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    ip_address = models.CharField(
        _("IP address"),
        max_length=16,
        help_text="IPv4 address",
    )
    username = models.CharField(
        _("username"),
        max_length=50,
        help_text="Username for SSH access",
    )

    def __str__(self) -> str:
        return f"{self.site.name!s} - {self.name!s}" or "instance object"


class Cluster(BaseModel):
    """
    Represents a collection of instances.

    Attributes:
        name (str): The name of the cluster.
        description (str): A description of the cluster (optional).
        instance (Instance): The instance associated with the cluster.
    """

    name = models.CharField(_("name"), max_length=64)
    description = models.TextField(_("description"), blank=True)
    instance = models.ManyToManyField(Instance)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return str(self.name) or "cluster object"
