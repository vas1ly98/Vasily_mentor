
from models import Product


def test_bad_product_model():
    # Корректные данные
    product = Product(name="Laptop", price="999.99", product=ProductType.NEW, year=2005,
                      manufacturer=Manufacturer(name="MSI"))

    assert isinstance(product, Product)
    assert product.name == "Laptop"
    assert product.price == 999.99
    assert product.product == ProductType.NEW
    assert product.year == 2005
    assert product.in_stock == False
    assert product.color == "black"

    # Неправильные данные (должна быть ошибка так как name должен быть длинее 3 символов)
    try:
        Product(name="x", price="999.99", product=ProductType.NEW, manufacturer=Manufacturer(name="MSI"))
    except ValueError:
        pass  # Ожидаем ошибку