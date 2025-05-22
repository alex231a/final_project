"""
Serializers for product data representation in the API.

This module defines serializers that transform Product model instances
into JSON representations for the Django REST Framework views.
"""

import logging
from oscar.apps.catalogue.models import Product  # pylint: disable=import-error
from oscar.apps.partner.strategy import Selector  # pylint: disable=import-error
from rest_framework import serializers

logger = logging.getLogger('shop_api')


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    Converts Product instances into JSON for API responses and vice versa.
    Includes basic fields such as ID, title, description, and price.
    """
    price = serializers.SerializerMethodField()

    class Meta:  # pylint: disable=too-few-public-methods
        """Class Meta"""
        model = Product
        fields = ['id', 'title', 'description', 'price']

    def get_price(self, obj):
        """
        Return the price including tax using Oscar's pricing strategy.
        """
        request = self.context.get('request')
        strategy = Selector().strategy(request=request)
        info = strategy.fetch_for_product(obj)
        if info.price.is_tax_known:
            price = str(info.price.incl_tax)
            logger.info("[get_price] Product ID %s - price incl. tax: %s",
                        obj.id, price)
        else:
            price = str(info.price.excl_tax)
            logger.info("[get_price] Product ID %s - price excl. tax: %s",
                        obj.id, price)

        return price
