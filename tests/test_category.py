import pytest
from unicodedata import category

from src.category import Category
from src.product import Product


def test_category_init(first_cat, second_cat):
    assert first_cat.name == "televisions"
    assert first_cat.description == "3D"
    assert len(first_cat.products_list) == 2

    assert second_cat.name == "fridge"
    assert second_cat.description == "embedded"
    assert len(second_cat.products_list) == 3

    assert first_cat.category_count == 2
    assert second_cat.category_count == 2

    assert first_cat.product_count == 5
    assert second_cat.product_count == 5

    assert Category.category_count == 2
    assert Category.product_count == 5


def test_category_product_property(first_cat):
    assert first_cat.products == ("Sony, 100.0 руб. Остаток: 2 шт.\nPhillips, 200.0 руб. Остаток: 1 шт.\n")


def test_category_add_product(first_cat):
    assert len(first_cat.products_list) == 2
    cat = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    first_cat.add_product(cat)
    assert len(first_cat.products_list) == 3


def test_category_str(first_cat):
    assert str(first_cat) == f"televisions, количество продуктов: 3шт."


def test_category_add_product_error(first_cat):
    with pytest.raises(TypeError):
        cat = 1
        first_cat.add_product(cat)


def test_category_add_product_smart(first_cat, smartphone1):
    first_cat.add_product(smartphone1)
    assert len(first_cat.products_list) == 3


def test_category_add_product_lawn(first_cat, lawngrass1):
    first_cat.add_product(lawngrass1)
    assert len(first_cat.products_list) == 3


def test_middle_price(first_cat, category_empty_product):
    assert category_empty_product.middle_price() == 0
    assert first_cat.middle_price() == 150

