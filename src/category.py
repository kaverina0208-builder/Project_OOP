from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        sum = 0
        for product in self.__products:
            sum += product.quantity
        return f"{self.name}, количество продуктов: {sum}шт."

    def add_product(self, product_new: Product):
        if isinstance(product_new, Product):
            self.__products.append(product_new)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        prod_str = ""
        for product in self.__products:
            prod_str += f"{str(product)}\n"
        return prod_str

    @property
    def products_list(self):
        return self.__products

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.products_list]) / len(self.products_list))
        except ZeroDivisionError:
            return 0
