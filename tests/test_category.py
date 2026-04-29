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
    assert first_cat.products == ("Sony, 123.0 руб. Остаток: 2 шт.\nPhillips, 156.0 руб. Остаток: 1 шт.\n")


def test_category_add_product(first_cat):
    assert len(first_cat.products_list) == 2
    cat = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    first_cat.add_product(cat)
    assert len(first_cat.products_list) == 3


def test_category_str(first_cat):
    assert str(first_cat) == f'televisions , количество продуктов: 3 шт.'