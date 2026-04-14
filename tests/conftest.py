import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def first_cat():
    return Category(
        name="televisions",
        description="3D",
        products=[Product("Sony", "rt-123", 123.0, 2), Product("Phillips", "yu-123", 156.0, 1)],
    )


@pytest.fixture
def second_cat():
    return Category(
        name="fridge",
        description="embedded",
        products=[
            Product("Sony", "12-29", 258.0, 2),
            Product("Sharp", "RT-13", 966.0, 1),
            Product("Phillips", "26-GH3", 566.0, 1),
        ],
    )


@pytest.fixture
def product():
    return Product("JVC", "HG-13", 256.0, 1)
