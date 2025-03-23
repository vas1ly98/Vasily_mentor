import random
import string
from faker import Faker
faker = Faker()

class DataGenerator:

    @staticmethod
    def generate_random_email():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"kek{random_string}@gmail.com"


    @staticmethod
    def generate_random_name():
        first_names = ["Иван", "Петр", "Саша", "Жора", "Петя"]
        last_names = ["Стручков", "Калашников", "Филюшов", "Иванов", "Петров"]
        sur_name = ["Васильевич", "Данилович", "Александрович", "Иванович", "Кирилович"]
        random_first_name = random.choice(first_names)
        random_last_name = random.choice(last_names)
        random_sur_name = random.choice(sur_name)
        return f"{random_first_name} {random_last_name} {random_sur_name}"


    @staticmethod
    def generate_random_password():
        """
        Генерация пароля, соответствующего требованиям:
        - Минимум 1 буква.
        - Минимум 1 цифра.
        - Допустимые символы.
        - Длина от 8 до 20 символов.
        """
        # Гарантируем наличие хотя бы одной буквы и одной цифры
        letters = random.choice(string.ascii_letters)  # Одна буква
        digits = random.choice(string.digits)  # Одна цифра

        # Дополняем пароль случайными символами из допустимого набора
        special_chars = "!?@#'."
        all_chars = string.ascii_letters + string.digits + special_chars
        remaining_length = random.randint(6, 12)  # Остальная длина пароля
        remaining_chars = ''.join(random.choices(all_chars, k=remaining_length))

        # Перемешиваем пароль для рандомизации
        password = list(letters + digits + remaining_chars)
        random.shuffle(password)
        final_password = ''.join(password)

        return final_password[:12]

