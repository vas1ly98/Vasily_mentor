



c = 10
while True:
    print(F'ТЕКУЩЕЯ C = {c}')
    c -= 1
    if c == 0:
        break

i = 1
while i > 0:
    for i in range(0, 11, 2):
        print(i)
    if i == 10:
        break

print("Имя\tдолжность\tзп")
print("Иван\tменеджер\t50000")
print("Петров\tпрограмист\t40000")

for i in range(1, 5):
    for j in range(1, 5):
        print(f'{i} + {j} = {i + j}', end = "\t")
    print()