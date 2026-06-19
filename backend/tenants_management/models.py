from django.db import models
from core.models import Sector
# Create your models here.
class Tenant(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    ]

    TIER_CHOICES = [
        ("FREE", "Free"),
        ("PRO", "Pro"),
        ("ENTERPRISE", "Enterprise"),
    ]

    name = models.CharField(max_length=255)

    tools=models.ManyToManyField("tools.Tool", related_name="tenants")

    tier = models.CharField(
        max_length=20,
        choices=TIER_CHOICES,
        default="FREE"
    )

    sectors = models.ManyToManyField(Sector, related_name="tenants")

    contact_name = models.CharField(max_length=255)

    contact_email = models.EmailField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
    
