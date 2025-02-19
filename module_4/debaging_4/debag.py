def inner_function(x):
    return x * 2  # Step Out здесь

def outer_function(a):
    b = inner_function(a + 1)  # Step Into здесь
    c = b * 3
    return c

result = outer_function(5)
print(result)