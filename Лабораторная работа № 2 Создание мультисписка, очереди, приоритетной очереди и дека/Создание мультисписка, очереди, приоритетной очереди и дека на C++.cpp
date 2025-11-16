// Мультисписок
#include <iostream>
#include <list>
int main() {
    std::list<int> multilist;
    // Добавление элементов
    multilist.push_back(10);
    multilist.push_back(20);
    multilist.push_front(5);
    multilist.insert(multilist.begin(), 5); // дубликат
    // Вывод
    std::cout << "Мультисписок: ";
    for (int x : multilist) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    // Удаление элемента
    multilist.remove(5); // удаляет все 5
    return 0;
}

// Очередь (FIFO)
#include <iostream>
#include <queue>
int main() {
    std::queue<int> q;
    // Добавление (enqueue)
    q.push(1);
    q.push(2);
    q.push(3);
    // Вывод размера
    std::cout << "Размер очереди: " << q.size() << std::endl;
    // Извлечение (dequeue)
    while (!q.empty()) {
        std::cout << q.front() << " ";
        q.pop();
    }
    std::cout << std::endl;
    return 0;
}

// Приоритетная очередь
#include <iostream>
#include <queue>
#include <vector>
int main() {
    // По умолчанию — max-heap (максимальный элемент вверху)
    std::priority_queue<int> pq;
    pq.push(10);
    pq.push(5);
    pq.push(20);
    pq.push(15);
    std::cout << "Приоритетная очередь (max-heap): ";
    while (!pq.empty()) {
        std::cout << pq.top() << " "; // извлекаем максимальный
        pq.pop();
    }
    std::cout << std::endl;
    // Min-heap (минимальный элемент вверху)
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_pq;
    min_pq.push(10);
    min_pq.push(5);
    min_pq.push(20);
    std::cout << "Приоритетная очередь (min-heap): ";
    while (!min_pq.empty()) {
        std::cout << min_pq.top() << " ";
        min_pq.pop();
    }
    std::cout << std::endl;
    return 0;
}

// Дек (двусторонняя очередь)
#include <iostream>
#include <deque>
int main() {
    std::deque<int> dq;
    // Добавление с концов
    dq.push_front(1);
    dq.push_back(2);
    dq.push_front(0);
    dq.push_back(3);
    // Вывод
    std::cout << "Дек: ";
    for (int x : dq) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    // Удаление с концов
    dq.pop_front();
    dq.pop_back();
    std::cout << "После удаления: ";
    for (int x : dq) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    // Доступ по индексу
    std::cout << "Элемент [1]: " << dq[1] << std::endl;
    return 0;
}
