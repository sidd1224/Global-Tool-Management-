from rest_framework import viewsets
from . import serializers
from . import models


class TenantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.tenantSerializer
    queryset = models.Tenant.objects.all()

    def get_queryset(self):
        queryset = models.Tenant.objects.all()

        tier = self.request.query_params.get("tier")
        sector = self.request.query_params.get("sector")
        status = self.request.query_params.get("status")
        search = self.request.query_params.get("search")

        if tier:
            queryset = queryset.filter(tier=tier)

        if sector:
            queryset = queryset.filter(
                sectors__name=sector
            )

        if status:
            queryset = queryset.filter(status=status)

        if search:
            queryset = queryset.filter(
                name__icontains=search
            )

        return queryset