
from rest_framework import viewsets
from rest_framework.views import APIView# Create your views here.
from .models import Tool
from .serializers import ToolSerializer
from rest_framework.response import Response


class ToolViewSet(viewsets.ModelViewSet):
    serializer_class = ToolSerializer
    queryset = Tool.objects.all()
    def get_queryset(self):
        queryset = Tool.objects.all()

        sector = self.request.query_params.get("sector")
        category = self.request.query_params.get("category")
        status = self.request.query_params.get("status")
        search = self.request.query_params.get("search")

        if sector:
            queryset = queryset.filter(
            sectors__name=sector
        )

        if category:
           queryset = queryset.filter(
            category=category
        )

        if status:
            queryset = queryset.filter(
            status=status
        )

        if search:
            queryset = queryset.filter(
            name__icontains=search
        )

        return queryset
    
class CategoryListView(APIView):
    def get(self,request):
        categories = Tool.objects.values_list("category", flat=True).distinct()
        return Response(categories)
    

