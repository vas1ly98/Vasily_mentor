text = "Python is awesome!"
print(text.upper())
text = text.replace('awesome', 'amasing')
print(text)

texts = "Hello, Python!"
print(texts[0:5])
print(texts[::2])

pi = 3.14159
rounded_pi = round(pi, 2)
print(rounded_pi)

quote = "Python is easy and powerful!"
quote = quote.replace('easy', 'fun').replace('powerful', 'versatile')
print(quote)

name = "Alice"
age = 25
print(f'{name} is {age} years old.')

data = "Price: 1234.5678 USD"
c = data[7:16]
b = float(c)
b = round(b, 2)
print(f"Rounded price: {b} USD")