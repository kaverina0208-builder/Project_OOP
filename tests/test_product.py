def test_product_init(product):
    assert product.name == "JVC"
    assert product.description == "HG-13"
    assert product.price == 256.0
    assert product.quantity == 1
