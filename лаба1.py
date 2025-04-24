def rabbit_pairs(n, k):
    # Начальные условия
    if n == 1 or n == 2:
        return 1
    # Рекурсивное вычисление
    return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)

# Ввод данных от пользователя
n = int(input("Введите номер месяца (n): "))
k = int(input("Введите количество пар потомков (k): "))

# Результат
print(f"Общее число пар кроликов на {n}-ый месяц: {rabbit_pairs(n, k)}")

