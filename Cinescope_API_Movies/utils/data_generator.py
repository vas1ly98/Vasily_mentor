import random
import string


class DataGenerator:

    @staticmethod
    def generate_random_movie():
        first_word = ['SUPER', 'WONDERFUL', 'NICE', 'GOOD', 'BEST', 'BAD']
        two_word =['NIGHTMARE', 'BOY', 'GIRL', 'MAN', 'WARRIOR']
        random_first_word = random.choice(first_word)
        random_two_word = random.choice(two_word)
        return f'{random_first_word}_{random_two_word}'

    @staticmethod
    def generate_random_description():
        movie_description = ['Фильм для мальчиков', 'Фильм для девочек', 'Фильм для всех']

        random_description = random.choice(movie_description)
        return f'{random_description}'

    @staticmethod
    def generate_random_email():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"kek{random_string}@gmail.com"


    @staticmethod
    def generate_random_name():
        first_names = ["John", "Jane", "Alex", "Emily", "Chris"]
        last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis"]
        random_first_name = random.choice(first_names)
        random_last_name = random.choice(last_names)
        return f"{random_first_name} {random_last_name}"


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
        special_chars = "?@#$%^&*_-+()[]{}><\\/|\"'.,:;"
        all_chars = string.ascii_letters + string.digits + special_chars
        remaining_length = random.randint(6, 18)  # Остальная длина пароля
        remaining_chars = ''.join(random.choices(all_chars, k=remaining_length))

        # Перемешиваем пароль для рандомизации
        password = list(letters + digits + remaining_chars)
        random.shuffle(password)

        return ''.join(password)

