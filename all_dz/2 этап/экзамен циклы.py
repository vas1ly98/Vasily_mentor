for i in range(1, 10):
    print(i)

print()

c = 10
while c != 0:
    print(c)
    c -= 1
print('счет завершен')

for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")

print()
print()

price = {'Зелье лечения': 100,
         'Зелье маны': 80,
         'Свиток скорости': 150,
         'Артефакт магии': 300}

tovar = input()
total = int(input())
if tovar in price:
    summa = price[tovar] * total
    print(f"Изначальная стоимость: {summa} золотых")
    if summa > 500:
        summa = summa * 0.8
        print("Гоблин говорит: 'Твоя скидка 20%! Покупай быстрее, пока я не передумал!')
     print(f"Итоговая стоимость: {summa:.2f} золотых")
else:
    price[tovar] not in price
    print("У меня такого нет, попробуй в другом месте!")
