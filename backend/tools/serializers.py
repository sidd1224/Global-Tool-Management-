from rest_framework import serializers
from .models import Tool
from core.models import Sector


class ToolSerializer(serializers.ModelSerializer):

    sectors = serializers.PrimaryKeyRelatedField(
        queryset=Sector.objects.all(),
        many=True
    )

    sector_names = serializers.StringRelatedField(
        source="sectors",
        many=True,
        read_only=True
    )

    class Meta:
        model = Tool
        fields = "__all__"