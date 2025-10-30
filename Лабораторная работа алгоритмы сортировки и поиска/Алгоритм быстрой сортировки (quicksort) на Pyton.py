def quicksort(arr):
    # Базовый случай: если массив содержит 0 или 1 элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr
    
    # Выбор опорного элемента (обычно средний элемент массива)
    pivot = arr[len(arr) // 2]
    
    # Формирование трех списков:
    # 1. Элементы меньше опорного
    # 2. Элементы равные опорному
    # 3. Элементы больше опорного
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    # Рекурсивно сортируем списки "less" и "greater",
    # а затем соединяем их вместе с "equal"
    return quicksort(less) + equal + quicksort(greater)

# Пример использования
numbers = [3, 6, 8, 10, 1, 2, 1]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)
