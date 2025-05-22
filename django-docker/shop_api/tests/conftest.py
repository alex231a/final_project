"""
Factory and fixture for creating Product instances in tests.

This module defines a factory using factory_boy to simplify the creation
of Product objects for testing purposes. It also provides a reusable
pytest fixture to generate test data in different scenarios.
"""

import pytest
from oscar.apps.catalogue.models import Product # pylint: disable=import-error
from factory.django import DjangoModelFactory # pylint: disable=import-error

class ProductFactory(DjangoModelFactory): # pylint: disable=too-few-public-methods
    """
    Factory for generating Product instances using default or custom values.

    Uses factory_boy's DjangoModelFactory to streamline test data creation.
    Default values:
    - title: "Test Product"
    - description: "Test Description"
    """
    class Meta: # pylint: disable=too-few-public-methods
        """Class Meta."""
        model = Product

    title = "Test Product"
    description = "Test Description"

@pytest.fixture
def product_factory():
    """
    Pytest fixture that returns a factory function to create Product instances.

    Example:
        product = product_factory(title="My Custom Product")

    Returns:
        Callable[..., Product]: A function that creates Product instances
                                with optional overridden fields.
    """
    def factory(**kwargs):
        return ProductFactory.create(**kwargs)
    return factory
