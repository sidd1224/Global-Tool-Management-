from . import models
from rest_framework import serializers


class tenantSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tenant
        fields="__all__"