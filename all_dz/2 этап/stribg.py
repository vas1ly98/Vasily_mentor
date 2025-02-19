from dataclasses import replace

text = "Hello, Python!"
print(text[0:5])
print(text[7:14])
print(text[3::])
print(text[2:12:3])
print(text[-1:3])


sentence = "PYTHON programming IS Fun"
sentence_cap = sentence.lower().upper()
print(sentence_cap.capitalize())       # 'ПРИВЕТ, МОСКВА'

phrase = "   Python   - это  круто!   "
phrase = phrase.replace("  ", " ").strip()
print(phrase)

text = "home/user/documents/python/lesson1"
words = text.split("/")  # ['Привет', 'Москва']
print(words)

sentence = "\\".join(words)  # 'Привет, Москва'
print(sentence)

a = 2
b = 2
print(pow(a,b))
