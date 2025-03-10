# import json
#
# from pydantic import BaseModel
#
#
# class Product(BaseModel):
#     name: str
#     price: float
#     in_stock: bool
#
# product = Product(name="Alice", price=25, in_stock=True)
#
# # 🔵 Сериализация в файл
# with open("product.json", "w") as file:
#     json.dump(product.model_dump(), file)
#
# # 🔵 Десериализация из файла
# with open("product.json", "r") as file:
#     product_data = json.load(file)
#     new_product = Product(**product_data)
#     print(new_product)
import allure  # Импортируем пакет allure
import pytest


@allure.step("Проверка сложения чисел {a} и {b}")
def check_addition(a, b, expected):
    with allure.step(f"Сложение {a} и {b}"):
        result = a + b
    with allure.step(f"Проверка результата {result} == {expected}"):
        assert result == expected

def test_addition():
    check_addition(2, 2, 4)
    check_addition(3, 5, 8)