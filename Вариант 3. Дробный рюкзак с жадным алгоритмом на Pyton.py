class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.unit_value = value / weight  # удельная стоимость

def fractional_knapsack(items, capacity):
    """
    Жадный алгоритм для дробного рюкзака.
    
    Параметры:
    - items: список объектов Item (вес, стоимость)
    - capacity: вместимость рюкзака (число)
    
    Возвращает:
    - max_value: максимальная стоимость, которую можно унести
    - selected: список взятых предметов с указанием доли (1 = целиком, <1 = часть)
    """
    # Сортируем предметы по убыванию удельной стоимости
    sorted_items = sorted(items, key=lambda x: x.unit_value, reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    selected = []
    
    for item in sorted_items:
        if remaining_capacity <= 0:
            break
        
        # Определяем, какую долю предмета можно взять
        if item.weight <= remaining_capacity:
            fraction = 1.0  # берём целиком
        else:
            fraction = remaining_capacity / item.weight  # берём часть
        
        # Добавляем стоимость взятой доли
        total_value += item.value * fraction
        remaining_capacity -= item.weight * fraction
        
        # Записываем взятый предмет и долю
        selected.append({
            'item': item,
            'fraction': fraction,
            'added_value': item.value * fraction,
            'added_weight': item.weight * fraction
        })
    
    return total_value, selected


# Пример использования
if __name__ == "__main__":
    # Создаём предметы: (вес, стоимость)
    items = []
    c = int(input('Введите количество предметов: '))
    for i in range(c):
        items.append(Item(float(input('Введите вес предмета: ')), float(input('Введите стоимость предмета: '))))
    capacity = float(input('Введите вместимость рюкзака: '))  # вместимость рюкзака
    
    max_value, selected_items = fractional_knapsack(items, capacity)
    
    print(f"Максимальная стоимость: {max_value:.2f}")
    print("Взятые предметы:")
    for entry in selected_items:
        item = entry['item']
        frac = entry['fraction']
        print(f"  Вес: {item.weight}, Стоимость: {item.value}, Доля: {frac:.2f}, "
              f"Добавленная стоимость: {entry['added_value']:.2f}, Вес: {entry['added_weight']:.2f}")
