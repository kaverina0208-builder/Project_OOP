class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# if __name__ == '__main__':
#     prod1 = Product('Sony', 'rt-123', 123.0, 2)
#     prod2 = Product('Phillips', 'yu-123', 156.0, 1)
#     prod3 = Product('JVC', 'KL-123', 563.0, 8)
