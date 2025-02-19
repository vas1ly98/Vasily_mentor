import math
from itertools import count


def greet(a):
    if a % 2 == 0:
        print('это число четное')
    else:
        print('число не четное')
    pass

def greet(width, height):
    if width > 0 and height > 0:
        print((width * height) * 0.5)
    elif width < 0 or height < 0:
        print("Некорректные значения")
    pass


def greet_person(name, age):
    print(f"Привет, {name}! Тебе {age} лет.")



def circle_area(pi, r):
    s = pi * (r ** 2)
    print(s)


def book_info(title, author, year, genre=None):
    print(f'Название: {title} '
          f'Автор: {author} '
          f'Год издания: {year} '
          f'Жанр: {genre}')

def max_of_two(a, b):
    if a > b:
        return a
    else:
         return b
    pass


def calculate_delivery_cost(weight, distance, fragile=False):
    dostavka = (weight * 10) + (5* distance)
    if dostavka < 200:
        return 'Закажите больше товаров'
    elif dostavka >= 200 and fragile == True:
        return dostavka * 1.5
    elif dostavka >= 200 and fragile == False:
        return dostavka
    pass

def filter_list(data:list, threshold:int):
    c = []
    for i in data:
        if int(i) >= threshold:
            c.append(int(i))
    return c


def analyze_numbers(numbers:list):
    return c = {'average': sum(numbers) / len(numbers),
                'min': min(numbers),
                'max': max(numbers)}
    

