from typing import List, Optional, Union


def multiply(c: int, b: int) -> int:
    return c * b

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Пользователь найден"
    return None

def process_input(value: Union[int, str]) -> str:
    return f"Ты передал: {value}"

def get_even_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 2 == 0]

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self: str) -> str:
        return f"Привет, меня зовут {self.name}!"


