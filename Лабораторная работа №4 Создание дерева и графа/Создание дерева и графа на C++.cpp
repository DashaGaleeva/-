// Граф
#include <iostream>
#include <vector>
class Graph {
private:
    int numVertices;                // Количество вершин
    std::vector<std::vector<int>> adjMatrix;  // Матрица смежности
public:
    // Конструктор: создаём граф с n вершинами
    Graph(int n) : numVertices(n) {
        adjMatrix.resize(n, std::vector<int>(n, 0));
    }
    // Добавить ребро между вершинами u и v (неориентированный граф)
    void addEdge(int u, int v) {
        if (u >= 0 && u < numVertices && v >= 0 && v < numVertices) {
            adjMatrix[u][v] = 1;
            adjMatrix[v][u] = 1;  // Для неориентированного графа
        } else {
            std::cerr << "Ошибка: вершина вне диапазона\n";
        }
    }
    // Удалить ребро между u и v
    void removeEdge(int u, int v) {
        if (u >= 0 && u < numVertices && v >= 0 && v < numVertices) {
            adjMatrix[u][v] = 0;
            adjMatrix[v][u] = 0;
        } else {
            std::cerr << "Ошибка: вершина вне диапазона\n";
        }
    }
    // Проверить, есть ли ребро между u и v
    bool hasEdge(int u, int v) const {
        if (u >= 0 && u < numVertices && v >= 0 && v < numVertices) {
            return adjMatrix[u][v] == 1;
        }
        return false;
    }
    // Вывести матрицу смежности
    void printMatrix() const {
        std::cout << "Матрица смежности:\n";
        for (int i = 0; i < numVertices; ++i) {
            for (int j = 0; j < numVertices; ++j) {
                std::cout << adjMatrix[i][j] << " ";
            }
            std::cout << "\n";
        }
    }
    // Получить список соседей вершины u
    std::vector<int> getNeighbors(int u) const {
        std::vector<int> neighbors;
        if (u >= 0 && u < numVertices) {
            for (int v = 0; v < numVertices; ++v) {
                if (adjMatrix[u][v] == 1) {
                    neighbors.push_back(v);
                }
            }
        }
        return neighbors;
    }
    // Получить количество вершин
    int getNumVertices() const {
        return numVertices;
    }
};
// Пример использования
int main() {
    // Создаём граф с 5 вершинами
    Graph g(5);
    // Добавляем рёбра
    g.addEdge(0, 1);
    g.addEdge(0, 4);
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 3);
    g.addEdge(3, 4);
    // Выводим матрицу
    g.printMatrix();
    // Проверяем наличие рёбер
    std::cout << "Есть ребро 0–1? " << (g.hasEdge(0, 1) ? "Да" : "Нет") << "\n";
    std::cout << "Есть ребро 0–2? " << (g.hasEdge(0, 2) ? "Да" : "Нет") << "\n";
    // Получаем соседей вершины 1
    std::vector<int> neighbors = g.getNeighbors(1);
    std::cout << "Соседи вершины 1: ";
    for (int n : neighbors) {
        std::cout << n << " ";
    }
    std::cout << "\n";
    return 0;
}

// Дерево
#include <iostream>
using namespace std;
// Структура узла дерева
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int value) : data(value), left(nullptr), right(nullptr) {}
};
// Класс бинарного дерева поиска
class BinaryTree {
private:
    TreeNode* root;
    // Вспомогательная функция для вставки узла (рекурсивная)
    TreeNode* insertRec(TreeNode* node, int value) {
        if (node == nullptr) {
            return new TreeNode(value);
        }
        if (value < node->data) {
            node->left = insertRec(node->left, value);
        } else if (value > node->data) {
            node->right = insertRec(node->right, value);
        }
        return node;
    }
    // Вспомогательная функция для обхода in‑order (рекурсивная)
    void inorderRec(TreeNode* node) {
        if (node != nullptr) {
            inorderRec(node->left);
            cout << node->data << " ";
            inorderRec(node->right);
        }
    }
    // Вспомогательная функция для поиска узла (рекурсивная)
    TreeNode* searchRec(TreeNode* node, int value) {
        if (node == nullptr || node->data == value) {
            return node;
        }
        if (value < node->data) {
            return searchRec(node->left, value);
        }
        return searchRec(node->right, value);
    }
    // Вспомогательная функция для нахождения минимального узла
    TreeNode* findMin(TreeNode* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }
    // Вспомогательная функция для удаления узла (рекурсивная)
    TreeNode* deleteRec(TreeNode* node, int value) {
        if (node == nullptr) {
            return node;
        }
        if (value < node->data) {
            node->left = deleteRec(node->left, value);
        } else if (value > node->data) {
            node->right = deleteRec(node->right, value);
        } else {
            // Узел найден: удаляем его
            if (node->left == nullptr) {
                TreeNode* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == nullptr) {
                TreeNode* temp = node->left;
                delete node;
                return temp;
            }
            // Узел имеет двух потомков: находим следующий по величине
            TreeNode* temp = findMin(node->right);
            node->data = temp->data;
            node->right = deleteRec(node->right, temp->data);
        }
        return node;
    }
public:
    BinaryTree() : root(nullptr) {}
    // Вставка узла
    void insert(int value) {
        root = insertRec(root, value);
    }
    // Обход in‑order (слева → корень → справа)
    void inorder() {
        inorderRec(root);
        cout << endl;
    }
    // Поиск узла
    bool search(int value) {
        return searchRec(root, value) != nullptr;
    }
    // Удаление узла
    void remove(int value) {
        root = deleteRec(root, value);
    }
    // Деструктор (очистка памяти)
    ~BinaryTree() {
        destroyTree(root);
    }
private:
    // Вспомогательная функция для очистки памяти (рекурсивная)
    void destroyTree(TreeNode* node) {
        if (node != nullptr) {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }
};
// Пример использования
int main() {
    BinaryTree tree;
    // Добавляем узлы
    tree.insert(50);
    tree.insert(30);
    tree.insert(70);
    tree.insert(20);
    tree.insert(40);
    tree.insert(60);
    tree.insert(80);
    // Обход in‑order
    cout << "In‑order обход: ";
    tree.inorder();  // Вывод: 20 30 40 50 60 70 80
    // Поиск узлов
    cout << "Поиск 40: " << (tree.search(40) ? "найден" : "не найден") << endl;
    cout << "Поиск 25: " << (tree.search(25) ? "найден" : "не найден") << endl;
    // Удаление узла
    tree.remove(20);
    cout << "После удаления 20 (in‑order): ";
    tree.inorder();  // Вывод: 30 40 50 60 70 80
    return 0;
}
