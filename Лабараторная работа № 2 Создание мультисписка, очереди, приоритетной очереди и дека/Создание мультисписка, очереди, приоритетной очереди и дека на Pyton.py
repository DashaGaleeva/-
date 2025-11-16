# Мультисписок (список списков)
class MultiList:
    def __init__(self):
        self.data = []
    def add_list(self, lst):
        """Добавить новый список"""
        self.data.append(lst)
    def get_list(self, index):
        """Получить список по индексу"""
        return self.data[index] if 0 <= index < len(self.data) else None
    def remove_list(self, index):
        """Удалить список по индексу"""
        if 0 <= index < len(self.data):
            del self.data[index]
    def size(self):
        """Количество списков"""
        return len(self.data)
    def display(self):
        """Показать все списки"""
        for i, lst in enumerate(self.data):
            print(f"Список {i}: {lst}")
# Пример использования
ml = MultiList()
ml.add_list([1, 2, 3])
ml.add_list(['a', 'b'])
ml.display()

# Очередь (FIFO)
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        """Проверить, пуста ли очередь"""
        return len(self.items) == 0
    def enqueue(self, item):
        """Добавить элемент в конец очереди"""
        self.items.append(item)
    def dequeue(self):
        """Удалить элемент из начала очереди"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)
    def front(self):
        """Посмотреть первый элемент"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0]
    def size(self):
        """Размер очереди"""
        return len(self.items)
    def display(self):
        """Показать очередь"""
        print("Очередь:", self.items)
# Пример использования
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()  # Очередь: [1, 2, 3]
print(q.dequeue())  # 1

# Приоритетная очередь
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0  # для сохранения порядка вставки при равных приоритетах
    def push(self, item, priority):
        """Добавить элемент с приоритетом"""
        # heapq использует min-heap, поэтому инвертируем приоритет
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        """Удалить элемент с наивысшим приоритетом"""
        if not self._queue:
            raise IndexError("Приоритетная очередь пуста")
        priority, index, item = heapq.heappop(self._queue)
        return item, -priority  # возвращаем исходный приоритет
    def is_empty(self):
        """Проверить, пуста ли очередь"""
        return len(self._queue) == 0
    def size(self):
        """Размер очереди"""
        return len(self._queue)
    def display(self):
        """Показать содержимое (не в порядке приоритета)"""
        temp = self._queue[:]
        items = []
        while temp:
            priority, index, item = heapq.heappop(temp)
            items.append((item, -priority))
        print("Приоритетная очередь:", items)
# Пример использования
pq = PriorityQueue()
pq.push("Задача A", 1)
pq.push("Задача B", 3)
pq.push("Задача C", 2)
pq.display()  # Приоритетная очередь: [('Задача B', 3), ('Задача C', 2), ('Задача A', 1)]
while not pq.is_empty():
    item, priority = pq.pop()
    print(f"Выполняю {item} (приоритет {priority})")

# Дек (двусторонняя очередь)
from collections import deque
class Deque:
    def __init__(self):
        self.items = deque()
    def is_empty(self):
        """Проверить, пуст ли дек"""
        return len(self.items) == 0
    def append_right(self, item):
        """Добавить в правый конец"""
        self.items.append(item)
    def append_left(self, item):
        """Добавить в левый конец"""
        self.items.appendleft(item)
    def pop_right(self):
        """Удалить с правого конца"""
        if self.is_empty():
            raise IndexError("Дек пуст")
        return self.items.pop()
    def pop_left(self):
        """Удалить с левого конца"""
        if self.is_empty():
            raise IndexError("Дек пуст")
        return self.items.popleft()
    def peek_right(self):
        """Посмотреть правый конец"""
        if self.is_empty():
            raise IndexError("Дек пуст")
        return self.items[-1]
    def peek_left(self):
        """Посмотреть левый конец"""
        if self.is_empty():
            raise IndexError("Дек пуст")
        return self.items[0]
    def size(self):
        """Размер дека"""
        return len(self.items)
    def display(self):
        """Показать дек"""
        print("Дек:", list(self.items))
# Пример использования
d = Deque()
d.append_right(1)
d.append_left(0)
d.append_right(2)
d.display()  # Дек: [0, 1, 2]
print(d.pop_left())   # 0
print(d.pop_right())  # 2
