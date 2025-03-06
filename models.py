# from pydantic import BaseModel, Field, validator
# from typing import Optional
#
# class Product(BaseModel):
#     name: str = Field(..., min_length=3, max_length=50, description="Название продукта")
#     price: float = Field(..., gt=0, description="Цена продукта")
#     in_stock: bool = Field(default=False, description="Есть ли в наличии")
#     color: str = "black"
#     year: Optional[int] = None
#     product: ProductType
#     manufacturer: Manufacturer