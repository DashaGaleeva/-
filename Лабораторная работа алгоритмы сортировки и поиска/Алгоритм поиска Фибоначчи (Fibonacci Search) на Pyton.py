def fibonacci_search(arr, target):
    def fib_gen(limit):
        """Генерирует числа Фибоначчи до указанного предела."""
        fib_sequence = [0, 1]
        while True:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            if next_fib > limit:
                break
            fib_sequence.append(next_fib)
        return fib_sequence[:-1]  # исключаем последнее число, так как оно превысило лимит

    # Генерируем последовательность Фибоначчи достаточной длины
    m = len(arr)
    fib_seq = fib_gen(m)

    offset = -1  # смещение для индексации
    k = len(fib_seq) - 1  # стартуем с наибольшего доступного числа Фибоначчи

    # Основной цикл поиска
    while k > 0:
        i = min(offset + fib_seq[k], m - 1)  # вычисляем индекс для проверки
        if arr[i] < target:
            # элемент меньше, идём вправо
            offset = i
            k -= 1
        elif arr[i] > target:
            # элемент больше, идём влево
            k -= 2
        else:
            # элемент найден
            return i

    # если элемент не найден
    return -1

# Пример использования
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
target = 85
result = fibonacci_search(arr, target)

if result != -1:
    print(f"Элемент {target} найден на индексе {result}.")
else:
    print(f"Элемент {target} не найден в массиве.")
