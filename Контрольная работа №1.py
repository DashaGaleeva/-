# Блочная (корзинная) сортировка
def bucket_sort(arr):
    # 1. Определим количество корзин (возьмём столько же, сколько элементов в массиве)
    buckets_count = len(arr)
    # 2. Создаём список пустых корзин
    buckets = [[] for _ in range(buckets_count)]
    # 3. Распределение элементов по корзинам
    for num in arr:
        # Нормализуем элемент в пределах [0, 1), учитывая максимальный элемент
        normalized_value = num / max(arr)
        # Вычисляем номер корзины, округлив нормализованное значение
        bucket_idx = int(normalized_value * (buckets_count - 1))
        buckets[bucket_idx].append(num)
    # 4. Сортируем каждую корзину индивидуально
    sorted_buckets = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)  # Используем встроенную сортировку Python
        sorted_buckets.extend(sorted_bucket)
    # 5. Возвращаем отсортированный массив
    return sorted_buckets
# Пример использования
numbers = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
sorted_numbers = bucket_sort(numbers)
print("Отсортированный массив:", sorted_numbers)

# Блинная сортировка
def flip(arr, k):
    # Перевертываем первые k элементов массива
    start = 0
    end = k
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def find_max(arr, n):
    # Находим индекс максимального элемента в первой n частях массива
    mi = 0
    for i in range(1, n):
        if arr[i] > arr[mi]:
            mi = i
    return mi
def pancake_sort(arr):
    current_size = len(arr)
    while current_size > 1:
        # Находим индекс максимального элемента в текущей части массива
        max_idx = find_max(arr, current_size)
        # Если максимальный элемент уже на вершине, просто опускаем его вниз
        if max_idx != current_size - 1:
            # Переворачиваем максимальный элемент на вершину
            flip(arr, max_idx)
            # Переворачиваем всю текущую часть массива, перемещая максимальный элемент вниз
            flip(arr, current_size - 1)
        # Уменьшаем размер рассматриваемой части массива
        current_size -= 1
# Пример использования
arr = [3, 6, 2, 7, 4, 1]
pancake_sort(arr)
print("Отсортированный массив:", arr)

# Сортировка бусинами
def bead_sort(arr):
    # Создаем виртуальную сетку из бусин
    grid = [[True if j < val else False for j in range(max(arr))] for val in arr]
    # Пусть бусы свободно "падают" вниз
    for col in range(len(grid[0])):
        count = sum(row[col] for row in grid)
        for row in range(count):
            grid[row][col] = True
        for row in range(count, len(grid)):
            grid[row][col] = False
    # Преобразовываем сетку обратно в отсортированный массив
    sorted_arr = [sum(col) for col in zip(*grid)]
    return sorted_arr
# Пример использования
numbers = [5, 3, 1, 7, 4]
sorted_numbers = bead_sort(numbers)
print("Отсортированный массив:", sorted_numbers)

# Поиск скачками
import math
def jump_search(arr, target):
    n = len(arr)                       # 1. Определяем длину массива
    step = int(math.sqrt(n))           # 2. Определяем оптимальный шаг поиска
    prev = 0                           # 3. Запоминаем последнюю точку остановки
    # 4. Производим поиск блоков с указанным шагом
    while arr[min(step, n)-1] < target:
        prev = step                     # 5. Переходим к следующему блоку
        step += int(math.sqrt(n))       # 6. Увеличение шага на sqrt(n)
        if prev >= n:                   # 7. Выход, если вышли за пределы массива
            return -1
    # 8. Проведение линейного поиска в найденном блоке
    while arr[prev] < target:
        prev += 1                       # 9. Линейный поиск внутри блока
        if prev == min(step, n):       # 10. Если достигли конца блока
            return -1
    # 11. Проверка точного соответствия
    if arr[prev] == target:
        return prev                     # 12. Вернуть индекс найденного элемента
    return -1                          # 13. Если элемент не найден
# Пример использования
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
target = 34
result = jump_search(arr, target)
if result != -1:
    print(f"Элемент {target} найден на индексе {result}.")
else:
    print(f"Элемент {target} не найден.")

# Экспоненциальный поиск
def exponential_search(arr, target):
    # 1. Проверяем первый элемент
    if arr[0] == target:
        return 0
    # 2. Удвоение шага до тех пор, пока не превысим массив или не найдем подходящее место
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    # 3. Если индекс превышает длину массива, ограничиваем его границей массива
    low = i // 2
    high = min(i, len(arr) - 1)
    # 4. Стандартный бинарный поиск в найденном диапазоне
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    # 5. Если элемент не найден
    return -1
# Пример использования
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
target = 34
result = exponential_search(arr, target)
if result != -1:
    print(f"Элемент {target} найден на индексе {result}.")
else:
    print(f"Элемент {target} не найден.")

# Тернарный поиск
def ternary_search(func, left, right, epsilon=1e-6):
    """
    func: Монотонная функция, чье экстремальное значение мы ищем.
    left: Левая граница интервала поиска.
    right: Правая граница интервала поиска.
    epsilon: Допустимая погрешность для остановки поиска.
    """
    while abs(right - left) > epsilon:
        # Делим интервал на три части
        third = (right - left) / 3
        left_third = left + third
        right_third = right - third
        # Проверяем, какая часть интервала содержит экстремум
        if func(left_third) < func(right_third):
            # Экстремум находится в левой трети
            right = right_third
        else:
            # Экстремум находится в правой трети
            left = left_third
    # Возвращаем координату экстремума
    return (left + right) / 2
# Пример использования
def f(x):
    # Пример функции: кубическое уравнение с экстремумом
    return x**3 - 6*x**2 + 9*x + 15
extremum_point = ternary_search(f, 0, 5)
print(f"Экстремум функции находится в точке x={extremum_point:.6f}, значение функции y={f(extremum_point):.6f}")
