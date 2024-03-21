from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    """
    A base model providing common fields.

    Attributes:
        created_at (DateField): The timestamp when the instance was created.
        updated_at (DateField): The timestamp when the instance was last updated.
        created_by (ForeignKey): The user who created the instance.
    """

    created_at = models.DateField(auto_now_add=True, null=False)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_created_by",
    )

    class Meta:
        abstract = True


class Zone(BaseModel):
    """
    Represents a zone.

    Attributes:
        name (CharField): The name of the zone.
    """

    name = models.CharField(max_length=64)
    lead = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_lead",
    )

    def __str__(self) -> str:
        return self.name


class District(BaseModel):
    """
    Represents a district.

    Attributes:
        name (CharField): The name of the district.
        zone (ForeignKey): The zone to which the district belongs.
    """

    name = models.CharField(max_length=64)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Site(models.Model):
    """
    Represents a site.

    Attributes:
        name (CharField): The name of the site.
        district (ForeignKey): The district to which the site belongs.
        ip_address (CharField): The IP address of the site (optional).
        username (CharField): The username for accessing the site (optional).
        password (CharField): The password for accessing the site (optional).
    """

    name = models.CharField(max_length=64)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        """
        Override the save method to call clean() before saving.
        """
        self.clean()
        super().save(*args, **kwargs)

    def clean(self):
        """
        Custom model validation method to ensure uniqueness of name within the district.
        """
        existing_sites = Site.objects.filter(name=self.name, district=self.district)
        if self.pk:  # If updating an existing instance, exclude self from the queryset
            existing_sites = existing_sites.exclude(pk=self.pk)
        if existing_sites.exists():
            error = "A site with the same name already exists in this district."
            raise ValidationError(
                error,
            )


class Instance(models.Model):
    """Virtual or metal host"""

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    ip_address = models.CharField(
        max_length=16,
        blank=True,
        help_text="IPv4 address for the instance",
    )
    username = models.CharField(
        max_length=50,
        blank=True,
        help_text="Username for ssh access",
    )

    def __str__(self) -> str:
        return self.name
