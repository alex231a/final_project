"""
Unit tests for ProductSerializer in the shop_api application.

This module contains tests for ensuring the ProductSerializer correctly
serializes Product instances, including the logic for retrieving price
information using Django Oscar's pricing strategy.
"""

from unittest.mock import MagicMock, patch
import pytest
from rest_framework.test import APIRequestFactory
from shop_api.serializers import ProductSerializer  # pylint: disable=import-error


@pytest.mark.django_db
def test_product_serializer_returns_price_with_tax(product_factory):
    """
    Test that ProductSerializer returns the correct price with tax.

    This test mocks Oscar's pricing strategy to simulate a product with a
    known tax-inclusive price. It verifies that the serializer outputs
    the expected price and other product fields.

    Steps:
    - Create a test product using the provided factory.
    - Create a mock request to pass into the serializer context.
    - Patch the Selector strategy to return a mocked price object.
    - Verify that the serializer returns the correct title, description,
    and price.

    Assertions:
    - title matches the created product.
    - description matches the created product.
    - price matches the mocked incl_tax value.
    """

    product = product_factory(title="Test Product",
                              description="Test Description")

    request = APIRequestFactory().get('/api/products/')
    context = {'request': request}

    mock_price = MagicMock()
    mock_price.is_tax_known = True
    mock_price.incl_tax = 123.45

    mock_info = MagicMock()
    mock_info.price = mock_price

    with patch('shop_api.serializers.Selector') as mock_selector:
        mock_selector().strategy().fetch_for_product.return_value = mock_info

        serializer = ProductSerializer(instance=product, context=context)
        data = serializer.data

        assert data['title'] == product.title
        assert data['description'] == product.description
        assert data['price'] == '123.45'
