from django.db import models

from core.models import Sector


class Tool(models.Model):

    STATUS_CHOICES = [
        ("DEPLOYED", "Deployed"),
        ("DRAFT", "Draft"),
        ("DISABLED", "Disabled"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()

    sectors = models.ManyToManyField(
    Sector,
    related_name="tools"
)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default="DRAFT")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


