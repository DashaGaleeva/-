Биноминальная куча (Binomial Heap)
class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.children = []  # список дочерних узлов
        self.parent = None
class BinomialHeap:
    def __init__(self):
        self.trees = []  # список корней биноминальных деревьев
    def merge_trees(self, t1, t2):
        """Объединяет два дерева одинаковой степени"""
        if t1.key > t2.key:
            t1, t2 = t2, t1  # t2 становится родителем
        t2.parent = t1
        t1.children.append(t2)
        return t1
    def union(self, other):
        """Объединяет две биноминальные кучи"""
        # Сливаем списки деревьев
        self.trees.extend(other.trees)
        self.trees.sort(key=lambda x: len(x.children))  # сортируем по степени
        # Проходим и объединяем деревья одинаковой степени
        i = 0
        while i < len(self.trees) - 1:
            if len(self.trees[i].children) == len(self.trees[i + 1].children):
                merged = self.merge_trees(self.trees[i], self.trees[i + 1])
                self.trees[i] = merged
                self.trees.pop(i + 1)
            else:
                i += 1
    def insert(self, key):
        """Добавляет элемент"""
        new_heap = BinomialHeap()
        new_heap.trees.append(BinomialNode(key))
        self.union(new_heap)
    def find_min(self):
        """Находит минимальный элемент"""
        if not self.trees:
            return None
        return min(tree.key for tree in self.trees)
    def extract_min(self):
        """Удаляет минимальный элемент"""
        if not self.trees:
            return None
        # Находим дерево с минимальным корнем
        min_tree = min(self.trees, key=lambda x: x.key)
        self.trees.remove(min_tree)
        # Создаём новую кучу из детей min_tree
        new_heap = BinomialHeap()
        for child in min_tree.children:
            child.parent = None
            new_heap.trees.append(child)
        # Объединяем с текущей кучей
        self.union(new_heap)
        return min_tree.key
# Пример использования:
bh = BinomialHeap()
bh.insert(10)
bh.insert(5)
bh.insert(20)
print(bh.find_min())      # 5
print(bh.extract_min())    # 5
print(bh.find_min())      # 10

# Куча Фибоначчи (Fibonacci Heap)
class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.left = self  # круговой двусвязный список
        self.right = self
        self.degree = 0
        self.marked = False
class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.root_list = None
        self.count = 0
    def insert(self, key):
        node = FibonacciNode(key)
        self._add_to_root_list(node)
        if self.min_node is None or node.key < self.min_node.key:
            self.min_node = node
        self.count += 1
        return node
    def _add_to_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list
            node.left = self.root_list.left
            self.root_list.left.right = node
            self.root_list.left = node
    def _remove_from_root_list(self, node):
        if node.right == node:  # единственный узел
            self.root_list = None
        else:
            node.left.right = node.right
            node.right.left = node.left
            if node == self.root_list:
                self.root_list = node.right
    def find_min(self):
        return self.min_node.key if self.min_node else None
    def extract_min(self):
        z = self.min_node
        if z is not None:
            # Добавляем детей z в корневой список
            if z.child:
                children = []
                child = z.child
                while True:
                    children.append(child)
                    child = child.right
                    if child == z.child:
                        break
                for child in children:
                    self._add_to_root_list(child)
                    child.parent = None
            # Удаляем z из корневого списка
            self._remove_from_root_list(z)
            # Обновляем min_node
            if z == self.root_list:
                self.min_node = None
                self.root_list = None
            else:
                self.min_node = z.right
                self._consolidate()
            self.count -= 1
            return z.key
        return None
    def _consolidate(self):
        A = [None] * self.count
        nodes = []
        current = self.root_list
        if current:
            while True:
                nodes.append(current)
                current = current.right
                if current == self.root_list:
                    break
        for w in nodes:
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.min_node = None
        for i in range(len(A)):
            if A[i] is not None:
                if self.min_node is None:
                    self.root_list = A[i]
                    self.min_node = A[i]
                else:
                    self._add_to_root_list(A[i])
                    if A[i].key < self.min_node.key:
                        self.min_node = A[i]
    def _link(self, y, x):
        self._remove_from_root_list(y)
        y.parent = x
        y.left = y
        y.right = y
        if x.child is None:
            x.child = y
        else:
            y.right = x.child
            y.left = x.child.left
            x.child.left.right = y
            x.child.left = y
        x.degree += 1
        y.marked = False
# Пример использования:
fh = FibonacciHeap()
fh.insert(10)
fh.insert(5)
fh.insert(20)
print(fh.find_min())       # 5
print(fh.extract_min())     # 5
print(fh.find_min())       # 10

# Хеш‑таблица (Hash Table)
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
    def _hash(self, key):
        return hash(key) %
