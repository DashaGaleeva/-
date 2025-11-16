# Граф
class Graph:
    def __init__(self):
        self.graph = {}  # словарь смежности
    def add_vertex(self, vertex):
        """Добавить вершину"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self, v1, v2):
        """Добавить ребро между вершинами v1 и v2"""
        # Добавляем обе вершины, если их нет
        self.add_vertex(v1)
        self.add_vertex(v2)
        # Добавляем смежность в обе стороны (неориентированный граф)
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    def remove_edge(self, v1, v2):
        """Удалить ребро между v1 и v2"""
        if v1 in self.graph and v2 in self.graph[v1]:
            self.graph[v1].remove(v2)
        if v2 in self.graph and v1 in self.graph[v2]:
            self.graph[v2].remove(v1)
    def get_neighbors(self, vertex):
        """Получить список смежных вершин"""
        return self.graph.get(vertex, [])
    def __str__(self):
        return str(self.graph)
" Пример использования
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
print(g)  # {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}

# Дерево
class BinaryTree:
    def __init__(self):
        self.tree = []  # Список для хранения узлов
    def insert(self, value):
        """Добавить узел в дерево (в конец списка)"""
        self.tree.append(value)
    def get_left_child(self, index):
        """Получить индекс левого потомка"""
        left_index = 2 * index + 1
        if left_index < len(self.tree):
            return left_index
        return None
    def get_right_child(self, index):
        """Получить индекс правого потомка"""
        right_index = 2 * index + 2
        if right_index < len(self.tree):
            return right_index
        return None
    def get_parent(self, index):
        """Получить индекс родителя"""
        if index == 0:
            return None  # Корень не имеет родителя
        return (index - 1) // 2
    def get_value(self, index):
        """Получить значение узла по индексу"""
        if 0 <= index < len(self.tree):
            return self.tree[index]
        return None
    def set_value(self, index, value):
        """Установить значение узла по индексу"""
        if 0 <= index < len(self.tree):
            self.tree[index] = value
    def is_empty(self):
        """Проверить, пустое ли дерево"""
        return len(self.tree) == 0
    def size(self):
        """Получить количество узлов"""
        return len(self.tree)
    def display(self):
        """Вывести дерево в виде списка"""
        print("Дерево (список):", self.tree)
" Пример использования
if __name__ == "__main__":
    tree = BinaryTree()
    # Добавляем узлы (в порядке обхода уровней)
    for value in [10, 5, 15, 3, 7, 12, 18]:
        tree.insert(value)
    tree.display()
    # Проверяем связи
    print(f"Корень (индекс 0): {tree.get_value(0)}")
    print(f!Левый потомок корня: {tree.get_value(tree.get_left_child(0))}")
    print(f!Правый потомок корня: {tree.get_value(tree.get_right_child(0))}")
    print(f"Родитель узла с индексом 3 (значение {tree.get_value(3)}): {tree.get_value(tree.get_parent(3))}")
