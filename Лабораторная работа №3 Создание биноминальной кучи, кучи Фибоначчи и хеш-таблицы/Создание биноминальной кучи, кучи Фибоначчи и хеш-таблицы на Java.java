// Биноминальная куча (Binomial Heap)
class BinomialHeapNode {
    int key;
    int degree;
    BinomialHeapNode parent;
    BinomialHeapDesktop sibling;
    BinomialHeapNode child;
    public BinomialHeapNode(int key) {
        this.key = key;
        this.degree = 0;
        this.parent = null;
        this.sibling = null;
        this.child = null;
    }
}
class BinomialHeap {
    private BinomialHeapNode root;
    public BinomialHeap() {
        root = null;
    }
    // Слияние двух биноминальных деревьев одинаковой степени
    private BinomialHeapNode mergeTrees(BinomialHeapNode a, BinomialHeapNode b) {
        if (a.key > b.key) {
            BinomialHeapNode temp = a;
            a = b;
            b = temp;
        }
        b.parent = a;
        b.sibling = a.child;
        a.child = b;
        a.degree++;
        return a;
    }
    // Объединение двух корней куч
    private BinomialHeapNode unionRoots(BinomialHeapNode h1, BinomialHeapNode h2) {
        if (h1 == null) return h2;
        if (h2 == null) return h1;
        BinomialHeapNode newRoot = null;
        BinomialHeapNode tail = null;
        while (h1 != null && h2 != null) {
            if (h1.degree <= h2.degree) {
                if (tail == null) {
                    newRoot = h1;
                } else {
                    tail.sibling = h1;
                }
                tail = h1;
                h1 = h1.sibling;
            } else {
                if (tail == null) {
                    newRoot = h2;
                } else {
                    tail.sibling = h2;
                }
                tail = h2;
                h2 = h2.sibling;
            }
        }
        if (h1 != null) tail.sibling = h1;
        if (h2 != null) tail.sibling = h2;
        return newRoot;
    }
    // Объединение двух биноминальных куч
    public void union(BinomialHeap other) {
        root = unionRoots(root, other.root);
        if (root == null) return;
        BinomialHeapNode prev = null;
        BinomialHeapNode curr = root;
        BinomialHeapNode next = curr.sibling;
        while (next != null) {
            if (curr.degree != next.degree || 
                (next.sibling != null && next.sibling.degree == curr.degree)) {
                prev = curr;
                curr = next;
            } else if (curr.key <= next.key) {
                curr.sibling = next.sibling;
                mergeTrees(curr, next);
            } else {
                if (prev == null) {
                    root = next;
                } else {
                    prev.sibling = next;
                }
                mergeTrees(next, curr);
                curr = next;
            }
            next = curr.sibling;
        }
    }
    // Вставка ключа
    public void insert(int key) {
        BinomialHeap tempHeap = new BinomialHeap();
        tempHeap.root = new BinomialHeapNode(key);
        union(tempHeap);
    }
    // Поиск минимального ключа
    public int getMin() {
        if (root == null) throw new IllegalStateException("Heap is empty");
        int min = root.key;
        BinomialHeapNode curr = root.sibling;
        while (curr != null) {
            if (curr.key < min) min = curr.key;
            curr = curr.sibling;
        }
        return min;
    }
    // Удаление минимального элемента
    public int extractMin() {
        if (root == null) throw new IllegalStateException("Heap is empty");
        // Находим узел с минимальным ключом
        BinomialHeapNode minNode = root;
        BinomialHeapNode prevMin = null;
        BinomialHeapNode curr = root;
        BinomialHeapNode prev = null;
        while (curr != null) {
            if (curr.key < minNode.key) {
                minNode = curr;
                prevMin = prev;
            }
            prev = curr;
            curr = curr.sibling;
        }
        // Удаляем minNode из списка корней
        if (prevMin == null) {
            root = minNode.sibling;
        } else {
            prevMin.sibling = minNode.sibling;
        }
        // Обрабатываем детей minNode
        BinomialHeap reversedChildren = reverseList(minNode.child);
        // Объединяем оставшуюся кучу с детьми minNode
        BinomialHeap tempHeap = new BinomialHeap();
        tempHeap.root = reversedChildren.root;
        union(tempHeap);
        return minNode.key;
    }
    // Разворот списка sibling
    private BinomialHeap reverseList(BinomialHeapNode head) {
        BinomialHeap result = new BinomialHeap();
        result.root = null;
        BinomialHeapNode curr = head;
        while (curr != null) {
            BinomialHeapNode next = curr.sibling;
            curr.sibling = result.root;
            result.root = curr;
            curr = next;
        }
        return result;
    }
    // Проверка пустоты
    public boolean isEmpty() {
        return root == null;
    }
}

// Куча Фибоначчи (Fibonacci Heap)
class FibonacciNode {
    int key;
    int degree;
    boolean marked;
    FibonacciNode parent;
    FibonacciNode child;
    FibonacciNode left;
    FibonacciNode right;
    public FibonacciNode(int key) {
        this.key = key;
        this.degree = 0;
        this.marked = false;
        this.parent = null;
        this.child = null;
        this.left = this;
        this.right = this;
    }
}
class FibonacciHeap {
    private FibonacciNode min;
    private int size;
    public FibonacciHeap() {
        min = null;
        size = 0;
    }
    // Вставка узла
    public void insert(int key) {
        FibonacciNode node = new FibonacciNode(key);
        if (min == null) {
            min = node;
        } else {
            concatenate(min, node);
            if (node.key < min.key) min = node;
        }
        size++;
    }
    // Конкатенация двух круговых списков
    private void concatenate(FibonacciNode a, FibonacciNode b) {
        FibonacciNode aRight = a.right;
        FibonacciNode bLeft = b.left;
        a.right = b;
        b.left = a;
        aRight.left = bLeft;
        bLeft.right = aRight;
    }
    // Объединение двух куч
    public void union(FibonacciHeap other) {
        if (other.min == null) return;
        if (this.min == null) {
            this.min = other.min;
        } else {
            concatenate(this.min, other.min);
            if (other.min.key < this.min.key) this.min = other.min;
        }
        this.size += other.size;
    }
    // Извлечение минимума
    public int extractMin() {
        if (min == null) throw new IllegalStateException("Heap is empty");
        FibonacciNode z = min;
        if (z.child != null) {
            // Добавляем детей z в корневой список
            FibonacciNode child = z.child;
            do {
                child.parent = null;
                child = child.right;
            } while (child != z.child);
        }
    }
}

// Хеш-таблица
import java.util.HashMap;
import java.util.Map;
public class HashTableExample {
    public static void main(String[] args) {
        // Создаём хеш‑таблицу
        HashMap<Integer, String> phoneBook = new HashMap<>();
        // Добавляем элементы
        phoneBook.put(1234567, "Андрей");
        phoneBook.put(1333567, "Денис");
        phoneBook.put(1444567, "Мария");
        // Получаем значение
        System.out.println("Владелец 1333567: " + phoneBook.get(1333567));
        // Перебираем все пары
        for (Map.Entry<Integer, String> entry : phoneBook.entrySet()) {
            System.out.println("Телефон: " + entry.getKey() +
                              ", Имя: " + entry.getValue());
        }
        // Проверяем размер
        System.out.println("Всего контактов: " + phoneBook.size());
    }
}
