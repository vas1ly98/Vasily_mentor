number = 0


c = 100
b = 300

if c > b:
    print(f'число, {c}, самое большое')
elif b > c:
    print(f'число, {b}, самое большое')
else:
    print(f'числа, {b}, и, {c}, не равны')


used_logins = ["user123", "hacker", "test_bot"]

new_login = used_logins[0]

if new_login in used_logins:
    print('такой пользователь уже есть')
else:
    print('такого пользователя надо зарегестрировать')

new_login = 'жора'
if new_login in used_logins:
    print('такой пользователь уже есть')
else:
    used_logins.append(new_login)
    print('такого пользователя надо зарегестрировать')
print(used_logins)


