from src.product import Product
import pytest


def test_product_init(product):
    assert product.name == "JVC"
    assert product.description == "HG-13"
    assert product.price == 256.0
    assert product.quantity == 1


def test_new_product():
    prod_dict = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    product_test = Product.new_product(prod_dict)
    product_test.name == "Samsung Galaxy S23 Ultra"
    product_test.description == "256GB, Серый цвет, 200MP камера"
    product_test.price == 180000.0
    product_test.quantity == 5


def test_price_setter(capsys, product):
    product.price = 0
    massage = capsys.readouterr()
    assert massage.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"

    product.price = 1000
    assert product.price == 1000


def test_product_str(product):
    assert str(product) == "JVC, 256.0 руб. Остаток: 1 шт."


def test_product_add(product, product2):
    assert product.price * product.quantity + product2.price * product2.quantity == 556


def test_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Sony"
    assert next(product_iterator).name == "Sharp"
    assert next(product_iterator).name == "Phillips"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_product_init_zero():
    with pytest.raises(ValueError) as e:
        prod_zero = Product("JVC", "HG-13", 100.0, 0)
