def restore_health(current_health, potion):
    max_health = 100
    if current_health + potion > max_health:
        return max_health
    else:
        return current_health + potion

print(restore_health(90, 15))  # Вывод: 100
print(restore_health(50, 30))  # Вывод: 80