from src.product import Product

class Category:
    name: str
    description: str
    product: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, product=None):
        self.name = name
        self.description = description
        self.product = product if product else []
        Category.category_count += 1
        Category.product_count += len(product) if product else 0

# if __name__ == '__main__':
#     prod1 = Product('Sony', 'rt-123', 123.0, 2)
#     prod2 = Product('Phillips', 'yu-123', 156.0, 1)
#     prod3 = Product('JVC', 'KL-123', 563.0, 8)
#
#     cat1 = Category('televisions', '3D', [prod1, prod2, prod3])
#
#     print(cat1.name)
#     print(cat1.description)
#     print(cat1.product)
#
#     print(cat1.category_count)
#     print(Category.product_count)