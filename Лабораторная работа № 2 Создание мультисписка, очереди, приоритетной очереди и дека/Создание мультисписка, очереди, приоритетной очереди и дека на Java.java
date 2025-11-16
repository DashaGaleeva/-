// Мультисписок (MultiList)
import java.util.*;
public class MultiList<T> {
    private List<List<T>> lists;
    public MultiList() {
        lists = new ArrayList<>();
    }
    // Добавить новый подсписок
    public void addList() {
        lists.add(new ArrayList<>());
    }
    // Добавить элемент в конкретный подсписок
    public void add(int index, T element) {
        if (index >= 0 && index < lists.size()) {
            lists.get(index).add(element);
        } else {
            throw new IndexOutOfBoundsException("Индекс подсписка вне диапазона");
        }
    }
    // Получить элемент из конкретного подсписка
    public T get(int listIndex, int elementIndex) {
        if (listIndex >= 0 && listIndex < lists.size()) {
            List<T> sublist = lists.get(listIndex);
            if (elementIndex >= 0 && elementIndex < sublist.size()) {
                return sublist.get(elementIndex);
            } else {
                throw new IndexOutOfBoundsException("Индекс элемента вне диапазона");
            }
        } else {
            throw new IndexOutOfBoundsException("Индекс подсписка вне диапазона");
        }
    }
    // Размер конкретного подсписка
    public int size(int index) {
        if (index >= 0 && index < lists.size()) {
            return lists.get(index).size();
        } else {
            throw new IndexOutOfBoundsException("Индекс подсписка вне диапазона");
        }
    }
    @Override
    public String toString() {
        return lists.toString();
    }
}
// Пример использования:
MultiList<String> multiList = new MultiList<>();
multiList.addList(); // Создаём первый подсписок
multiList.add(0, "Элемент 1");
multiList.add(0, "Элемент 2");
System.out.println(multiList); // [[Элемент 1, Элемент 2]]

// Очередь (Queue)
public class Queue<T> {
    private T[] data;
    private int front;   // Указатель на начало очереди
    private int rear;    // Указатель на конец очереди
    private int size;    // Текущий размер
    private final int capacity;
    public Queue(int capacity) {
        this.capacity = capacity;
        data = (T[]) new Object[capacity];
        front = 0;
        rear = -1;
        size = 0;
    }
    public boolean isEmpty() {
        return size == 0;
    }
    public boolean isFull() {
        return size == capacity;
    }
    public void enqueue(T element) {
        if (isFull()) {
            throw new IllegalStateException("Очередь переполнена");
        }
        rear = (rear + 1) % capacity;
        data[rear] = element;
        size++;
    }
    public T dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("Очередь пуста");
        }
        T element = data[front];
        front = (front + 1) % capacity;
        size--;
        return element;
    }
    public T peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("Очередь пуста");
        }
        return data[front];
    }
    public int size() {
        return size;
    }
    @Override
    public String toString() {
        if (isEmpty()) return "[]";
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < size; i++) {
            int idx = (front + i) % capacity;
            sb.append(data[idx]);
            if (i < size - 1) sb.append(", ");
        }
        sb.append("]");
        return sb.toString();
    }
}
// Пример использования:
Queue<Integer> queue = new Queue<>(3);
queue.enqueue(1);
queue.enqueue(2);
System.out.println(queue.dequeue()); // 1
System.out.println(queue); // [2]

// Приоритетная очередь (PriorityQueue)
public class PriorityQueue<T extends Comparable<T>> {
    private T[] heap;
    private int size;
    private final int capacity;
    public PriorityQueue(int capacity) {
        this.capacity = capacity;
        heap = (T[]) new Comparable[capacity];
        size = 0;
    }
    public boolean isEmpty() {
        return size == 0;
    }
    public boolean isFull() {
        return size == capacity;
    }
    public void insert(T element) {
        if (isFull()) {
            throw new IllegalStateException("Очередь переполнена");
        }
        heap[size] = element;
        siftUp(size);
        size++;
    }
    public T extractMin() {
        if (isEmpty()) {
            throw new NoSuchElementException("Очередь пуста");
        }
        T min = heap[0];
        heap[0] = heap[size - 1];
        size--;
        siftDown(0);
        return min;
    }
    public T peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("Очередь пуста");
        }
        return heap[0];
    }
    private void siftUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[index].compareTo(heap[parent]) >= 0) break;
            swap(index, parent);
            index = parent;
        }
    }
    private void siftDown(int index) {
        while (true) {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int smallest = index;
            if (left < size && heap[left].compareTo(heap[smallest]) < 0) {
              smallest = left;
            }
            if (right < size && heap[right].compareTo(heap[smallest]) < 0) {
                smallest = right;
            }
            if (smallest == index) break;
            swap(index, smallest);
            index = smallest;
        }
    }
    private void swap(int i, int j) {
        T temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }
    public int size() {
        return size;
    }
    @Override
    public String toString() {
        return Arrays.toString(Arrays.copyOf(heap, size));
    }
}
// Пример использования:
PriorityQueue<Integer> pq = new PriorityQueue<>(5);
pq.insert(10);
pq.insert(5);
pq.insert(20);
System.out.println(pq.extractMin()); // 5
System.out.println(pq); // [10, 20]

// Дек (Deque — двусторонняя очередь)
public class Deque<T> {
    private T[] data;
    private int front;
    private int rear;
    private int size;
    private final int capacity;
    public Deque(int capacity) {
        this.capacity = capacity;
        data = (T[]) new Object[capacity];
        front = 0;
        rear = 0;
        size = 0;
    }
    public boolean isEmpty() {
        return size == 0;
    }
    public boolean isFull() {
        return
