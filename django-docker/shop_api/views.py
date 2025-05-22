"""
API views for exposing product catalogue data.

Provides a viewset that allows read-only access to the product list
and detail endpoints via the Django REST Framework.
"""

import logging
from oscar.apps.catalogue.models import Product  # pylint: disable=import-error
from rest_framework import viewsets

from .serializers import ProductSerializer

logger = logging.getLogger('shop_api')


class ProductViewSet(# pylint: disable=too-many-ancestors
    viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides read-only access to Product resources.

    This viewset supports:
    - Listing all products (GET /api/products/)
    - Retrieving a specific product by ID (GET /api/products/{id}/)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        logger.info("[ProductViewSet:list] User %s requested product list",
                    request.user)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        logger.info(
            "[ProductViewSet:retrieve] User %s requested product ID %s",
            request.user, product_id)
        return super().retrieve(request, *args, **kwargs)
