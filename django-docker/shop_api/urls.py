"""
URL routing for the product API endpoints.

Registers the ProductViewSet using Django REST Framework's router
and exposes the `/api/products/` endpoints.
"""

from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = router.urls
