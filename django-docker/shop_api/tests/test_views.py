"""
Integration tests for Product API views in the shop_api application.

These tests validate the behavior of the read-only ProductViewSet,
including the ability to list products and retrieve individual product
details via the Django REST Framework.
"""

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_product_list_view_returns_products(product_factory):
    """
    Test that the product list view returns all created products.

    This test creates two products using a factory and sends a GET request
    to the product list endpoint. It checks that:
    - The response status is 200 (OK)
    - Both product titles are present in the response data
    """
    product_factory(title="Product 1")
    product_factory(title="Product 2")

    client = APIClient()
    response = client.get('/api/v1/products/')

    assert response.status_code == 200

    titles = [product['title'] for product in response.data]
    assert "Product 1" in titles
    assert "Product 2" in titles


@pytest.mark.django_db
def test_product_detail_view_returns_single_product(product_factory):
    """
    Test that the product detail view returns the correct product.

    This test creates a single product and sends a GET request to its detail
    endpoint. It verifies that:
    - The response status is 200 (OK)
    - The returned product title matches the created product
    """
    product = product_factory(title="Single Product")

    client = APIClient()
    response = client.get(f'/api/v1/products/{product.id}/')
    assert response.status_code == 200
    assert response.data['title'] == "Single Product"
