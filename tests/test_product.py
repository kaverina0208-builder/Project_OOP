from itertools import product

from src.product import Product


def test_product_init(product):
    assert product.name == "JVC"
    assert product.description == "HG-13"
    assert product.price == 256.0
    assert product.quantity == 1


def test_new_product():
    prod_dict = {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}
    product_test = Product.new_product(prod_dict)
    product_test.name == 'Samsung Galaxy S23 Ultra'
    product_test.description == '256GB, Серый цвет, 200MP камера'
    product_test.price == 180000.0
    product_test.quantity == 5


def test_price_setter(capsys, product):
    product.price = 0
    massage = capsys.readouterr()
    assert massage.out.strip() == 'Цена не должна быть нулевая или отрицательная'

    product.price = 25
    assert product.price == 25