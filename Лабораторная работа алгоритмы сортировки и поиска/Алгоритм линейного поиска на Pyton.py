def linear_search(arr, target):
    """
    Линейный поиск элемента 'target' в списке 'arr'.
    Возвращает индекс элемента, если он найден, иначе None.
    """
    # Проходим по каждому элементу массива
    for index in range(len(arr)):  
        # Если текущий элемент совпадает с искомым
        if arr[index] == target:      
            # Возвращаем индекс найденного элемента
            return index              
    # Если элемент не найден, возвращаем None
    return None                      

# Пример использования
my_list = [4, 2, 7, 1, 9, 3]
search_element = 7

# Вызов функции поиска
found_index = linear_search(my_list, search_element)

# Вывод результата
if found_index is not None:
    print(f"Элемент {search_element} найден на индексе {found_index}.")
else:
    print(f"Элемент {search_element} не найден.")
