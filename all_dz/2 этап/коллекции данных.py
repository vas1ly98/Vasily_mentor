a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
assert len(c) > 5
print(c)


numbers = [10, 20, 40, 50]
numbers.insert(2, 30)
print(numbers)
numbers.clear()
print(numbers)

v = [1, 2, 3]
z = ["a", "b", "c"]
j = [True, False]
p = []
p.append(v)
p.append(z)
p.append(j)
print(p)
print(p[1][1])
last_item = p[0][0].pop()
assert last_item == 3
print((last_item))



