from tests.conftest import product


def test_category_init(first_cat, second_cat):
    assert first_cat.name == 'televisions'
    assert first_cat.description == '3D'
    assert len(first_cat.product) == 2

    assert second_cat.name == 'fridge'
    assert second_cat.description == 'embedded'
    assert len(second_cat.product) == 3

    assert first_cat.category_count == 2
    assert second_cat.category_count == 2

    assert first_cat.product_count == 5
    assert second_cat.product_count == 5
