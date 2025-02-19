n = int(input())
b = int(input())
c = input()
j = '+, , , /, %, //, *'
if c in j and c == '+':
    print(n + b)
elif c in j and с == '/':
    print(n / b)
elif c in j and с == '-':
    print(n - b)
elif c in j and с == '%':
    print(n % b)
elif c in j and с == '//':
    print(n // b)
elif c in j and с == '*':
    print(n * b)
else:
    print('poka')