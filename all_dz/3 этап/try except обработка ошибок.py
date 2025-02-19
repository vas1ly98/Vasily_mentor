def add(a, b):
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя!")
    return a / b

try:
    print(add(10, 1))
except ZeroDivisionError as e:
    print("Ошибка:", e)


def read_file(filename):
    try:
        if not filename.strip():  # Проверяем, что имя файла не пустое
            raise ValueError("Имя файла не может быть пустым.")

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content

    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


# Пример использования
file_name = input("Введите имя файла: ")
content = read_file(file_name)

if content:
    print("\nСодержимое файла:")
    print(content)


def arithmetic(numbers: list):
    results = []

    for num in numbers:
        try:
            result = 100 / num  # Делим 100 на число
            results.append(result)
        except ZeroDivisionError:
            print(f"Ошибка: деление на ноль (число {num} пропущено).")
        except TypeError:
            print(f"Ошибка: некорректный тип данных ({num} пропущен).")

    return results  # Возвращаем список результатов
#Обработка ошибок должна быть внутри функции — иначе при первой ошибке выполнение остановится.

# Пример использования
print(arithmetic([1, 3, 2, 44, 123213, 55, 0, "abc", 1, 6, 77]))

