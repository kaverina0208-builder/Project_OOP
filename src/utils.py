import json
import os
from idlelib.iomenu import encoding

from src.product import Product
from src.category import Category

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "products.json")

def read_json(path: str) -> dict:
    # full_path = os.path.abspath(path)
    with open(path, 'r', encoding='UTF-8') as file:
        result = json.load(file)
    return result


if __name__ == '__main__':
    print(read_json(PATH_TO_FILE))
