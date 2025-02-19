def restore_health(current_health, poiton):
    max_health = 100
    if current_health + poiton > max_health:
        return max_health
    else:
        return current_health + poiton

print(restore_health(90, 15))  # Вывод: 100
print(restore_health(50, 30))  # Вывод: 80