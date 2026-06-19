from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ToolViewSet, CategoryListView

router = DefaultRouter()
router.register(r"tools", ToolViewSet)

urlpatterns = [
    path(
        "tools/categories/",
        CategoryListView.as_view(),
        name="category-list"
    ),
]

urlpatterns += router.urls