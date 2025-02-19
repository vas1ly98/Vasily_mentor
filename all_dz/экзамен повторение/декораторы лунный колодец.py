# Декоратор для усиления восстановления здоровья
def health_boost(func):
    def wrapper(current_health, health_restore, hero_level):
        # Усиление восстановления для героев высокого уровня
        if hero_level > 10:
            health_restore *= 2
        return func(current_health, health_restore)
    return wrapper

# Функция восстановления здоровья
@health_boost
def drink_from_well(current_health, health_restore):
    max_health = 100
    # Рассчитываем итоговое здоровье
    new_health = current_health + health_restore
    if new_health > max_health:
        new_health = max_health
    return new_health

# Пример использования
hero_health = drink_from_well(current_health=80, health_restore=15, hero_level=12)
print(hero_health)  # Вывод: 100

hero_health = drink_from_well(current_health=50, health_restore=20, hero_level=8)
print(hero_health)  # Вывод: 70