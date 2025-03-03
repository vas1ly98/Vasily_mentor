import json

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    in_stock: bool

product = Product(name="Alice", price=25, in_stock=True)

# 🔵 Сериализация в файл
with open("product.json", "w") as file:
    json.dump(product.model_dump(), file)

# 🔵 Десериализация из файла
with open("product.json", "r") as file:
    product_data = json.load(file)
    new_product = Product(**product_data)
    print(new_product)
