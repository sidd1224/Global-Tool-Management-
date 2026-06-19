from rest_framework import serializers
from .models import Tool

class ToolSerializer(serializers.ModelSerializer):

    sectors = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Tool
        fields = "__all__"