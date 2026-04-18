import json
import os
from src.product import Product
from src.category import Category


ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "products.json")


def read_json(path: str) -> dict:
    # full_path = os.path.abspath(path)
    with open(path, "r", encoding="UTF-8") as file:
        result = json.load(file)
    return result


def create_objects_from_json(result):
    categories = []
    for cat in result:
        products = []
        for product in cat["products"]:
            products.append(Product(**product))
        cat["products"] = products
        categories.append(Category(**cat))
    return categories


if __name__ == "__main__":
    categories_obj = create_objects_from_json((read_json(PATH_TO_FILE)))

    print(categories_obj[0].name)
    print(categories_obj[0].products)
