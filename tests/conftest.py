import pytest
from src.product import Product
from src.category import Category
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


@pytest.fixture
def first_cat():
    return Category(
        name="televisions",
        description="3D",
        products=[Product("Sony", "rt-123", 100.0, 2), Product("Phillips", "yu-123", 200.0, 1)],
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


@pytest.fixture
def product2():
    return Product("JVC", "HG-13", 100.0, 3)


@pytest.fixture
def product_iterator(second_cat):
    return ProductIterator(second_cat)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawngrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_empty_product():
    return Category(name="processor", description="AD-2", products=[])
